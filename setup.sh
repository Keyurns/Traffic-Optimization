#!/bin/bash

# Traffic Video Processor - Setup Script
# Run with: bash setup.sh

echo "🚦 Traffic Video Processor - Setup Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv yolov8_env

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source yolov8_env/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To run the application:"
echo "1. Activate virtual environment: source yolov8_env/bin/activate"
echo "2. Start web server: python web_uploader.py"
echo "3. Open browser: http://localhost:5001"
echo ""
echo "Happy traffic analysis! 🚦✨"
