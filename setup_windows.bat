@echo off
echo ========================================
echo  Traffic Video Processor - Windows Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv yolov8_env
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment created
echo.

REM Activate virtual environment
echo Activating virtual environment...
call yolov8_env\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo ✓ Pip upgraded
echo.

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install requirements
    pause
    exit /b 1
)
echo ✓ Requirements installed
echo.

REM Install ultralytics
echo Installing ultralytics...
pip install ultralytics
if errorlevel 1 (
    echo ERROR: Failed to install ultralytics
    pause
    exit /b 1
)
echo ✓ Ultralytics installed
echo.

REM Download YOLO model
echo Downloading YOLO model...
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
if errorlevel 1 (
    echo WARNING: Failed to download YOLO model
    echo You may need to download it manually later
)
echo ✓ YOLO model ready
echo.

echo ========================================
echo  Setup Complete! 🎉
echo ========================================
echo.
echo To start the application:
echo 1. Double-click 'start_server.bat'
echo 2. Or run: start_server.bat
echo 3. Open http://localhost:5001 in your browser
echo.
echo To install dependencies only:
echo 1. Run: install_dependencies.bat
echo.
pause
