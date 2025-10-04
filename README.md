# 🚦 Traffic Video Processor - YOLO v8

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![YOLO](https://img.shields.io/badge/YOLO-v8-green.svg)](https://ultralytics.com)
[![Flask](https://img.shields.io/badge/Flask-2.3+-red.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web-based traffic video analysis tool that uses YOLO v8 to detect and count vehicles (cars, trucks, buses, motorcycles, bicycles) and people in traffic videos. Features real-time processing, cumulative counting, and an intuitive web interface.

## 🎥 Demo

![Traffic Video Processor Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Traffic+Video+Processor+Demo)

*Upload a traffic video and watch real-time vehicle detection with cumulative counting!*

## ✨ Features

- **🎯 Multi-Object Detection**: Detects cars, trucks, buses, motorcycles, bicycles, and people
- **📊 Real-time Statistics**: Live vehicle counting with cumulative totals
- **🎛️ Adjustable Confidence**: Slider to fine-tune detection sensitivity
- **🌐 Web Interface**: Easy-to-use drag-and-drop video upload
- **📈 Detailed Analytics**: Frame-by-frame and cumulative breakdowns
- **💾 Export Results**: Download processed videos and statistics
- **🔄 Reset Counters**: Clear cumulative counts when needed

## 🚀 Quick Start

### Prerequisites

- **macOS** (tested on macOS 24.5.0) or **Windows 10/11**
- **Python 3.8+** (Python 3.13 recommended)
- **Git** (for cloning)

### 🍎 macOS Installation

1. **Clone or Download the Project**
   ```bash
   # If you have git, clone the repository
   git clone <repository-url>
   cd "Traffic optimization"
   
   # Or simply download and extract the project folder
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv yolov8_env
   source yolov8_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install ultralytics opencv-python flask werkzeug
   ```

4. **Download YOLO Model** (if not already present)
   ```bash
   # The yolov8n.pt model should already be in your project folder
   # If not, it will be downloaded automatically on first run
   ```

### 🪟 Windows Installation

**Option 1: Automated Setup (Recommended)**
1. Download the project folder
2. Double-click `setup_windows.bat`
3. Follow the on-screen instructions

**Option 2: Manual Setup**
1. Open Command Prompt as Administrator
2. Navigate to project folder: `cd "C:\path\to\Traffic-Video-Processor"`
3. Run: `python -m venv yolov8_env`
4. Run: `yolov8_env\Scripts\activate`
5. Run: `pip install -r requirements.txt`
6. Run: `pip install ultralytics`

**📖 For detailed Windows instructions, see [WINDOWS_SETUP.md](WINDOWS_SETUP.md)**

### Running the Application

#### macOS
1. **Activate Virtual Environment**
   ```bash
   source yolov8_env/bin/activate
   ```

2. **Start the Web Server**
   ```bash
   python web_uploader.py
   ```

#### Windows
**Option 1: Double-click `start_server.bat`**
**Option 2: Run in Command Prompt**
```cmd
yolov8_env\Scripts\activate
python web_uploader.py
```

#### Both Platforms
3. **Open Your Browser**
   - Go to: `http://localhost:5001`
   - The web interface will load automatically

## 📁 Project Structure

```
Traffic optimization/
├── 📄 README.md                    # This file
├── 📄 WINDOWS_SETUP.md            # Detailed Windows setup guide
├── 🐍 web_uploader.py             # Main Flask web application
├── 🧠 yolov8n.pt                  # YOLO v8 model file
├── 📁 src/
│   └── 🐍 simple_detector.py      # Core detection logic
├── 📁 templates/
│   └── 🌐 index.html              # Web interface template
├── 📁 uploads/                    # Uploaded videos (auto-created)
├── 📁 outputs/                    # Processed videos (auto-created)
├── 📁 yolov8_env/                 # Python virtual environment
├── 🖼️ bus.jpg                     # Sample test image
├── 🪟 setup_windows.bat           # Windows automated setup
├── 🪟 start_server.bat            # Windows server launcher
├── 🪟 install_dependencies.bat    # Windows dependency installer
├── 💻 setup_windows.ps1           # Windows PowerShell setup
└── 💻 start_server.ps1            # Windows PowerShell launcher
```

## 🎮 How to Use

### 1. **Upload Video**
- Drag and drop a video file onto the upload area
- Or click "Choose Video File" to browse
- Supported formats: MP4, AVI, MOV, MKV, WMV, FLV (Max: 500MB)

### 2. **Adjust Detection Settings**
- Use the **Confidence Slider** to adjust detection sensitivity:
  - **Lower values (0.1-0.3)**: More detections, including motorcycles
  - **Higher values (0.6-0.9)**: Fewer false positives
  - **Recommended**: Start with 0.3 for motorcycles, 0.5 for general use

### 3. **Process Video**
- Click "Upload & Process" to start analysis
- Watch real-time progress and statistics
- Processing time depends on video length and resolution

### 4. **View Results**
- **Current Frame Count**: Vehicles detected in current frame
- **Cumulative Total**: Total vehicles detected throughout video
- **Vehicle Breakdown**: Count by type (person, bicycle, car, truck, bus, motorcycle)
- **Download**: Get processed video with detection overlays

## 🎯 Detection Types

| Type | Icon | Color | Description |
|------|------|-------|-------------|
| 🚶 Person | Magenta | Human detection |
| 🚲 Bicycle | Orange | Two-wheeled bicycles |
| 🚗 Car | Blue | Passenger vehicles |
| 🚛 Truck | Green | Large commercial vehicles |
| 🚌 Bus | Red | Public transport buses |
| 🏍️ Motorcycle | Cyan | Two-wheeled motorcycles |

## ⚙️ Configuration

### Confidence Thresholds
- **Motorcycles**: 0.2-0.4 (lower for better detection)
- **General Use**: 0.3-0.5 (balanced detection)
- **High Accuracy**: 0.6-0.8 (fewer false positives)

### Video Requirements
- **Formats**: MP4, AVI, MOV, MKV, WMV, FLV
- **Max Size**: 500MB
- **Resolution**: Any (higher resolution = longer processing time)
- **Duration**: Any length (processing time scales with duration)

## 🔧 Troubleshooting

### Common Issues

1. **"command not found: python"**
   ```bash
   # Make sure to activate virtual environment first
   source yolov8_env/bin/activate
   ```

2. **"Port 5001 is in use"**
   ```bash
   # Kill existing processes
   lsof -ti:5001 | xargs kill -9
   # Or restart your terminal
   ```

3. **"Module not found" errors**
   ```bash
   # Reinstall dependencies
   pip install ultralytics opencv-python flask werkzeug
   ```

4. **Poor motorcycle detection**
   - Lower confidence threshold to 0.2-0.3
   - Ensure good video quality and lighting
   - Motorcycles are smaller and harder to detect

### Performance Tips

- **Faster Processing**: Lower video resolution
- **Better Detection**: Higher video quality and lighting
- **Memory Issues**: Process shorter video segments
- **GPU Acceleration**: Install CUDA-compatible PyTorch (optional)

## 📊 Technical Details

### Dependencies
- **ultralytics**: YOLO v8 implementation
- **opencv-python**: Video processing
- **flask**: Web framework
- **werkzeug**: WSGI utilities

### System Requirements
- **RAM**: 4GB+ recommended
- **Storage**: 2GB+ free space
- **CPU**: Multi-core recommended for faster processing

## 🚀 Advanced Usage

### Command Line Processing
```bash
# Process a single video file
python -c "
from src.simple_detector import SimpleVehicleDetector
detector = SimpleVehicleDetector(confidence_threshold=0.3)
detector.process_video('input_video.mp4', 'output_folder')
"
```

### Custom Detection Classes
Edit `src/simple_detector.py` to modify detection classes:
```python
self.vehicle_classes = {
    0: 'person',      # Human detection
    1: 'bicycle',     # Bicycle detection
    2: 'car',         # Car detection
    3: 'motorcycle',  # Motorcycle detection
    5: 'bus',         # Bus detection
    7: 'truck'        # Truck detection
}
```

## 📝 License

This project is for educational and research purposes. Please ensure you have the right to process any videos you upload.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the project.

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed correctly
3. Verify your video format is supported
4. Try with a different confidence threshold

---

**Happy Traffic Analysis! 🚦✨**