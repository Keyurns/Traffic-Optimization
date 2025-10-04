#!/usr/bin/env python3
"""
Simple Web Interface for Traffic Video Upload and Processing
Upload video, see live detection, and download results
"""

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import os
import cv2
import threading
import time
from werkzeug.utils import secure_filename
import json
from pathlib import Path

# Import our simple detector
from src.simple_detector import SimpleVehicleDetector

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

# Create directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Global variables for processing
processing_status = {
    'is_processing': False,
    'progress': 0,
    'current_frame': 0,
    'total_frames': 0,
    'detected_vehicles': 0,
    'vehicle_counts': {'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0},
    'message': 'Ready to process video'
}

detector = None

def init_detector():
    """Initialize the vehicle detector"""
    global detector
    try:
        detector = SimpleVehicleDetector(confidence_threshold=0.5)
        return True
    except Exception as e:
        print(f"Error initializing detector: {e}")
        return False

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    
    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Get confidence threshold from form
    confidence = float(request.form.get('confidence', 0.3))
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Start processing in background
        thread = threading.Thread(target=process_video, args=(filepath, filename, confidence))
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Video uploaded and processing started',
            'filename': filename
        })

@app.route('/status')
def get_status():
    """Get processing status"""
    return jsonify(processing_status)

@app.route('/download/<filename>')
def download_file(filename):
    """Download processed video"""
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/preview/<filename>')
def preview_video(filename):
    """Preview processed video"""
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(filepath):
        return send_file(filepath)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/reset', methods=['POST'])
def reset_counters():
    """Reset cumulative counters"""
    global detector
    if detector:
        detector.reset_counters()
        processing_status['cumulative_total'] = 0
        processing_status['cumulative_counts'] = {'person': 0, 'bicycle': 0, 'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0}
        return jsonify({'success': True, 'message': 'Counters reset successfully'})
    else:
        return jsonify({'error': 'Detector not initialized'}), 400

def process_video(filepath, filename, confidence=0.3):
    """Process video in background"""
    global processing_status, detector
    
    try:
        processing_status['is_processing'] = True
        processing_status['message'] = 'Initializing...'
        processing_status['progress'] = 0
        
        # Initialize detector with custom confidence
        detector = SimpleVehicleDetector(confidence_threshold=confidence)
        
        processing_status['message'] = 'Opening video...'
        
        # Open video
        cap = cv2.VideoCapture(filepath)
        if not cap.isOpened():
            processing_status['message'] = 'Error: Could not open video'
            processing_status['is_processing'] = False
            return
        
        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        processing_status['total_frames'] = total_frames
        processing_status['message'] = f'Processing {total_frames} frames...'
        
        # Setup output video
        output_filename = f"processed_{filename}"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        # Reset statistics
        processing_status['detected_vehicles'] = 0
        processing_status['vehicle_counts'] = {'person': 0, 'bicycle': 0, 'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0}
        processing_status['cumulative_total'] = 0
        processing_status['cumulative_counts'] = {'person': 0, 'bicycle': 0, 'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0}
        
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process frame
            annotated_frame, stats = detector.process_frame(frame)
            
            # Add vehicle count overlay
            cv2.putText(annotated_frame, f"Current: {stats.total_vehicles} | Total: {stats.cumulative_total}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Write frame
            out.write(annotated_frame)
            
            # Update statistics
            frame_count += 1
            processing_status['current_frame'] = frame_count
            processing_status['detected_vehicles'] += stats.total_vehicles
            processing_status['cumulative_total'] = stats.cumulative_total
            processing_status['cumulative_counts'] = stats.cumulative_by_type.copy()
            
            # Update frame-by-frame counts (reset each frame)
            processing_status['vehicle_counts'] = stats.vehicles_by_type.copy()
            
            # Update progress
            progress = (frame_count / total_frames) * 100
            processing_status['progress'] = progress
            
            # Update message
            processing_status['message'] = f'Processing frame {frame_count}/{total_frames} ({progress:.1f}%)'
            
            time.sleep(0.01)  # Small delay to allow status updates
        
        # Cleanup
        cap.release()
        out.release()
        
        # Generate summary
        summary = {
            'total_frames': frame_count,
            'total_vehicles': processing_status['detected_vehicles'],
            'cumulative_total': processing_status['cumulative_total'],
            'average_vehicles_per_frame': processing_status['detected_vehicles'] / frame_count if frame_count > 0 else 0,
            'vehicle_breakdown': processing_status['cumulative_counts'],  # Use cumulative for final breakdown
            'cumulative_breakdown': processing_status['cumulative_counts'],
            'output_file': output_filename
        }
        
        # Save summary
        summary_path = os.path.join(app.config['OUTPUT_FOLDER'], f"summary_{filename}.json")
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Complete
        processing_status['message'] = 'Processing completed!'
        processing_status['is_processing'] = False
        processing_status['output_file'] = output_filename
        
    except Exception as e:
        processing_status['message'] = f'Error: {str(e)}'
        processing_status['is_processing'] = False

if __name__ == '__main__':
    print("🚦 Traffic Video Processor - Web Interface")
    print("=" * 50)
    print("Starting web server...")
    print("Open your browser and go to: http://localhost:5001")
    print("Press Ctrl+C to stop")
    print()
    
    app.run(host='0.0.0.0', port=5001, debug=True)
