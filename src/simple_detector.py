"""
Simple Vehicle Detection for Video Processing
Uses YOLO v8 for vehicle detection, classification, and counting
"""

import cv2
import numpy as np
from ultralytics import YOLO
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class DetectionStats:
    """Simple detection statistics"""
    total_vehicles: int
    vehicles_by_type: Dict[str, int]
    confidence: float
    cumulative_total: int = 0
    cumulative_by_type: Dict[str, int] = None
    
    def __post_init__(self):
        if self.cumulative_by_type is None:
            self.cumulative_by_type = {key: 0 for key in self.vehicles_by_type.keys()}

class SimpleVehicleDetector:
    """Simple vehicle detector for video processing"""
    
    def __init__(self, model_path: str = "yolov8n.pt", confidence_threshold: float = 0.3):
        """
        Initialize the detector
        
        Args:
            model_path: Path to YOLO model
            confidence_threshold: Minimum confidence for detections
        """
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold
        
        # Cumulative counters
        self.cumulative_total = 0
        self.cumulative_by_type = {'person': 0, 'bicycle': 0, 'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0}
        
        # Vehicle and human classes we're interested in (COCO dataset)
        self.vehicle_classes = {
            0: 'person',      # Human detection
            1: 'bicycle',     # Bicycle detection
            2: 'car',
            3: 'motorcycle', 
            5: 'bus',
            7: 'truck'
        }
        
        # Colors for different vehicle types and humans
        self.colors = {
            'person': (255, 0, 255),    # Magenta
            'bicycle': (255, 165, 0),   # Orange
            'car': (255, 0, 0),         # Blue
            'truck': (0, 255, 0),       # Green
            'bus': (0, 0, 255),         # Red
            'motorcycle': (255, 255, 0) # Cyan
        }
    
    def detect_vehicles(self, frame: np.ndarray) -> Tuple[np.ndarray, DetectionStats]:
        """
        Detect vehicles in a frame
        
        Args:
            frame: Input image frame
            
        Returns:
            Tuple of (annotated_frame, detection_stats)
        """
        # Run YOLO detection
        results = self.model(frame, conf=self.confidence_threshold, verbose=False)
        
        # Initialize statistics
        vehicle_counts = {"person": 0, "bicycle": 0, "car": 0, "truck": 0, "bus": 0, "motorcycle": 0}
        annotated_frame = frame.copy()
        
        # Process detections
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    # Get class ID and confidence
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    
                    # Check if it's a vehicle or person class
                    if class_id in self.vehicle_classes:
                        vehicle_type = self.vehicle_classes[class_id]
                        vehicle_counts[vehicle_type] += 1
                        
                        # Update cumulative counters
                        self.cumulative_by_type[vehicle_type] += 1
                        self.cumulative_total += 1
                        
                        # Debug: Print detection info (uncomment for debugging)
                        # print(f"Detected: {vehicle_type} (class {class_id}) with confidence {confidence:.2f}")
                        
                        # Get bounding box coordinates
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                        
                        # Draw bounding box
                        color = self.colors.get(vehicle_type, (255, 255, 255))
                        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
                        
                        # Draw label
                        label = f"{vehicle_type}: {confidence:.2f}"
                        label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
                        
                        # Draw label background
                        cv2.rectangle(annotated_frame, (x1, y1 - label_size[1] - 10), 
                                     (x1 + label_size[0], y1), color, -1)
                        
                        # Draw label text
                        cv2.putText(annotated_frame, label, (x1, y1 - 5), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Create statistics
        total_vehicles = sum(vehicle_counts.values())
        stats = DetectionStats(
            total_vehicles=total_vehicles,
            vehicles_by_type=vehicle_counts,
            confidence=self.confidence_threshold,
            cumulative_total=self.cumulative_total,
            cumulative_by_type=self.cumulative_by_type.copy()
        )
        
        return annotated_frame, stats
    
    def process_frame(self, frame: np.ndarray) -> Tuple[np.ndarray, DetectionStats]:
        """
        Process a single frame (alias for detect_vehicles)
        
        Args:
            frame: Input frame
            
        Returns:
            Tuple of (annotated_frame, detection_stats)
        """
        return self.detect_vehicles(frame)
    
    def reset_counters(self):
        """Reset cumulative counters"""
        self.cumulative_total = 0
        self.cumulative_by_type = {'person': 0, 'bicycle': 0, 'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0}
