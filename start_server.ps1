# Traffic Video Processor - Start Server (PowerShell)
# Run this script to start the web server

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Traffic Video Processor - Starting Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "yolov8_env\Scripts\Activate.ps1")) {
    Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run 'setup_windows.bat' or 'setup_windows.ps1' first" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

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

# Check if web_uploader.py exists
if (-not (Test-Path "web_uploader.py")) {
    Write-Host "ERROR: web_uploader.py not found!" -ForegroundColor Red
    Write-Host "Please make sure you're in the correct directory" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Start the server
Write-Host "Starting Traffic Video Processor server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "🌐 Web Interface: http://localhost:5001" -ForegroundColor Green
Write-Host "📁 Upload videos through the web interface" -ForegroundColor White
Write-Host "🛑 Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

try {
    python web_uploader.py
} catch {
    Write-Host ""
    Write-Host "Server stopped." -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to exit"
