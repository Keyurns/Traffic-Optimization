# Traffic Video Processor - Windows PowerShell Setup
# Run this script in PowerShell as Administrator if needed

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Traffic Video Processor - Windows Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
try {
    python -m venv yolov8_env
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to create virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
try {
    & "yolov8_env\Scripts\Activate.ps1"
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to activate virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip
Write-Host "✓ Pip upgraded" -ForegroundColor Green
Write-Host ""

# Install requirements
Write-Host "Installing requirements..." -ForegroundColor Yellow
try {
    pip install -r requirements.txt
    Write-Host "✓ Requirements installed" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to install requirements" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Install ultralytics
Write-Host "Installing ultralytics..." -ForegroundColor Yellow
try {
    pip install ultralytics
    Write-Host "✓ Ultralytics installed" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to install ultralytics" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Download YOLO model
Write-Host "Downloading YOLO model..." -ForegroundColor Yellow
try {
    python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
    Write-Host "✓ YOLO model ready" -ForegroundColor Green
} catch {
    Write-Host "WARNING: Failed to download YOLO model" -ForegroundColor Yellow
    Write-Host "You may need to download it manually later" -ForegroundColor Yellow
}

Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Setup Complete! 🎉" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the application:" -ForegroundColor White
Write-Host "1. Double-click 'start_server.bat'" -ForegroundColor Yellow
Write-Host "2. Or run: .\start_server.ps1" -ForegroundColor Yellow
Write-Host "3. Open http://localhost:5001 in your browser" -ForegroundColor Yellow
Write-Host ""
Write-Host "To install dependencies only:" -ForegroundColor White
Write-Host "1. Run: .\install_dependencies.ps1" -ForegroundColor Yellow
Write-Host ""

Read-Host "Press Enter to exit"
