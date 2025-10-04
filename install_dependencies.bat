@echo off
echo ========================================
echo  Installing Dependencies Only
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "yolov8_env\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run 'setup_windows.bat' first
    echo.
    pause
    exit /b 1
)

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
echo  Dependencies Installed! ✅
echo ========================================
echo.
echo To start the application:
echo 1. Run: start_server.bat
echo 2. Open http://localhost:5001 in your browser
echo.
pause
