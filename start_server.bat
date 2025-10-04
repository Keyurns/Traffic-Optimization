@echo off
echo ========================================
echo  Traffic Video Processor - Starting Server
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

REM Check if web_uploader.py exists
if not exist "web_uploader.py" (
    echo ERROR: web_uploader.py not found!
    echo Please make sure you're in the correct directory
    echo.
    pause
    exit /b 1
)

REM Start the server
echo Starting Traffic Video Processor server...
echo.
echo 🌐 Web Interface: http://localhost:5001
echo 📁 Upload videos through the web interface
echo 🛑 Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

python web_uploader.py

echo.
echo Server stopped.
pause
