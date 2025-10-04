# 🪟 Windows Setup Guide - Traffic Video Processor

This guide will help you set up and run the Traffic Video Processor on Windows 10/11.

## 📋 Prerequisites

- **Windows 10 or 11**
- **Python 3.8 or higher** (Download from [python.org](https://www.python.org/downloads/))
- **Git** (Download from [git-scm.com](https://git-scm.com/download/win))
- **At least 4GB RAM** (8GB recommended)
- **Webcam or video files** for testing

## 🚀 Quick Setup (Automated)

### Step 1: Download the Project
```cmd
git clone https://github.com/your-username/Traffic-Video-Processor.git
cd Traffic-Video-Processor
```

### Step 2: Run the Setup Script
```cmd
setup_windows.bat
```

**That's it!** The script will handle everything automatically.

## 🔧 Manual Setup (Step by Step)

### Step 1: Open Command Prompt as Administrator
1. Press `Windows + R`
2. Type `cmd`
3. Press `Ctrl + Shift + Enter` (to run as administrator)

### Step 2: Navigate to Project Directory
```cmd
cd "C:\path\to\your\Traffic-Video-Processor"
```

### Step 3: Create Virtual Environment
```cmd
python -m venv yolov8_env
```

### Step 4: Activate Virtual Environment
```cmd
yolov8_env\Scripts\activate
```

### Step 5: Upgrade pip
```cmd
python -m pip install --upgrade pip
```

### Step 6: Install Dependencies
```cmd
pip install -r requirements.txt
pip install ultralytics
```

### Step 7: Download YOLO Model (if not present)
```cmd
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

## 🎬 How to Run

### Method 1: Using the Web Interface (Recommended)

1. **Activate the virtual environment:**
   ```cmd
   yolov8_env\Scripts\activate
   ```

2. **Start the web server:**
   ```cmd
   python web_uploader.py
   ```

3. **Open your web browser:**
   - Go to: `http://localhost:5001`
   - Upload a video file
   - Watch real-time detection!

### Method 2: Using Command Line

1. **Activate the virtual environment:**
   ```cmd
   yolov8_env\Scripts\activate
   ```

2. **Run detection on a video:**
   ```cmd
   python src\simple_detector.py --video "path\to\your\video.mp4" --output "output_video.mp4"
   ```

## 🎯 Windows-Specific Features

### Batch Files for Easy Running

#### `start_server.bat`
```batch
@echo off
echo Starting Traffic Video Processor...
call yolov8_env\Scripts\activate
python web_uploader.py
pause
```

#### `install_dependencies.bat`
```batch
@echo off
echo Installing dependencies for Traffic Video Processor...
call yolov8_env\Scripts\activate
pip install -r requirements.txt
pip install ultralytics
echo Installation complete!
pause
```

### PowerShell Scripts (Alternative)

#### `start_server.ps1`
```powershell
Write-Host "Starting Traffic Video Processor..." -ForegroundColor Green
& "yolov8_env\Scripts\Activate.ps1"
python web_uploader.py
```

## 🔧 Troubleshooting Windows Issues

### Issue 1: "python is not recognized"
**Solution:**
```cmd
# Add Python to PATH or use full path
C:\Python39\python.exe -m venv yolov8_env
```

### Issue 2: "pip is not recognized"
**Solution:**
```cmd
python -m pip install --upgrade pip
```

### Issue 3: "Permission denied" when creating virtual environment
**Solution:**
1. Run Command Prompt as Administrator
2. Or use a different directory (e.g., `C:\Users\YourName\Desktop\`)

### Issue 4: "Port 5001 is already in use"
**Solution:**
```cmd
# Find what's using the port
netstat -ano | findstr :5001

# Kill the process (replace PID with actual process ID)
taskkill /PID <process_id> /F
```

### Issue 5: "ModuleNotFoundError" for ultralytics
**Solution:**
```cmd
# Make sure virtual environment is activated
yolov8_env\Scripts\activate

# Reinstall ultralytics
pip uninstall ultralytics
pip install ultralytics
```

### Issue 6: Slow performance on Windows
**Solutions:**
1. **Close unnecessary programs**
2. **Use SSD storage** for better I/O
3. **Increase virtual memory:**
   - Right-click "This PC" → Properties → Advanced System Settings
   - Performance Settings → Advanced → Virtual Memory
   - Set to "System managed size"

## 🎮 Windows-Specific Usage Tips

### 1. Using Windows File Explorer
- **Drag and drop** video files directly into the web interface
- **Supported formats:** MP4, AVI, MOV, WMV, MKV

### 2. Windows Performance Optimization
```cmd
# Set high performance power plan
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```

### 3. Windows Defender Exclusions
Add these folders to Windows Defender exclusions:
- `yolov8_env\`
- `runs\`
- `output\`

### 4. Windows Task Scheduler (Optional)
Set up automatic startup:
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger: "When I log on"
4. Action: Start a program
5. Program: `C:\path\to\your\project\start_server.bat`

## 📊 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 | Windows 11 |
| **RAM** | 4GB | 8GB+ |
| **Storage** | 2GB free | 5GB+ free |
| **CPU** | Intel i3/AMD Ryzen 3 | Intel i5/AMD Ryzen 5+ |
| **GPU** | Integrated | Dedicated GPU |

## 🚀 Quick Start Commands

### Complete Setup (Copy & Paste)
```cmd
git clone https://github.com/your-username/Traffic-Video-Processor.git
cd Traffic-Video-Processor
python -m venv yolov8_env
yolov8_env\Scripts\activate
pip install -r requirements.txt
pip install ultralytics
python web_uploader.py
```

### Daily Usage
```cmd
cd "C:\path\to\Traffic-Video-Processor"
yolov8_env\Scripts\activate
python web_uploader.py
```

## 🎯 Windows Shortcuts

### Create Desktop Shortcut
1. Right-click on desktop → New → Shortcut
2. Location: `C:\path\to\your\project\start_server.bat`
3. Name: "Traffic Video Processor"

### Pin to Taskbar
1. Run the application
2. Right-click on the Command Prompt icon in taskbar
3. Select "Pin to taskbar"

## 📱 Windows Mobile/Tablet Support

The web interface works on:
- **Windows tablets** (Surface, etc.)
- **Windows phones** (if still using Windows 10 Mobile)
- **Any device** with a web browser

## 🔄 Updates and Maintenance

### Update Dependencies
```cmd
yolov8_env\Scripts\activate
pip install --upgrade -r requirements.txt
```

### Update YOLO Model
```cmd
yolov8_env\Scripts\activate
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### Clean Up
```cmd
# Remove old output files
del /s /q output\*
del /s /q runs\*

# Remove virtual environment (if needed)
rmdir /s /q yolov8_env
```

## 🆘 Getting Help

### Windows Event Viewer
Check for errors:
1. Press `Windows + R`
2. Type `eventvwr.msc`
3. Look under "Windows Logs" → "Application"

### Windows Performance Monitor
Monitor system resources:
1. Press `Windows + R`
2. Type `perfmon`
3. Add counters for CPU, Memory, Disk

### Common Windows Error Codes
- **Error 0x80070005**: Permission denied → Run as Administrator
- **Error 0x80070002**: File not found → Check file paths
- **Error 0x80070020**: Port in use → Change port or kill process

---

## 🎉 You're Ready!

Your Traffic Video Processor is now ready to run on Windows! 

**Next Steps:**
1. Run `start_server.bat` or follow the manual setup
2. Open `http://localhost:5001` in your browser
3. Upload a video and start detecting vehicles!

**Need help?** Check the main README.md or create an issue on GitHub.

---

*Made with ❤️ for Windows users*
