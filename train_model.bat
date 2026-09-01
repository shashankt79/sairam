@echo off
REM Setup and train freight forecasting model
REM This batch file handles Python setup and runs the training pipeline

setlocal enabledelayedexpansion

cd /d "C:\Users\thont\Desktop\sairam-ai"

echo.
echo ════════════════════════════════════════════════════════════════
echo   🚀 SAIL FREIGHT FORECASTING - MODEL TRAINING SETUP
echo ════════════════════════════════════════════════════════════════
echo.

REM Try to find Python
for /f "tokens=*" %%i in ('where python 2^>nul') do set PYTHON_PATH=%%i
if not defined PYTHON_PATH (
    for /f "tokens=*" %%i in ('where python3 2^>nul') do set PYTHON_PATH=%%i
)

if not defined PYTHON_PATH (
    echo ❌ Python not found in PATH
    echo.
    echo 💡 Quick Fix Options:
    echo.
    echo Option 1: Install Python from python.org (recommended)
    echo   - Download from https://www.python.org/downloads/
    echo   - IMPORTANT: Check "Add python.exe to PATH" during install
    echo   - Then run this script again
    echo.
    echo Option 2: Use Replit (no local setup needed)
    echo   - Go to https://replit.com
    echo   - Create new Python project
    echo   - Upload train_model_synthetic.py
    echo   - Click "Run"
    echo.
    pause
    exit /b 1
)

echo ✓ Found Python at: %PYTHON_PATH%
%PYTHON_PATH% --version

echo.
echo 📦 Installing required packages...
echo.

REM Install packages
%PYTHON_PATH% -m pip install --upgrade pip --quiet >nul 2>&1
%PYTHON_PATH% -m pip install pandas numpy scikit-learn xgboost --quiet

if errorlevel 1 (
    echo ❌ Package installation failed
    pause
    exit /b 1
)

echo ✓ Packages installed successfully
echo.

REM Run training
echo ════════════════════════════════════════════════════════════════
echo 🤖 Starting Model Training...
echo ════════════════════════════════════════════════════════════════
echo.

%PYTHON_PATH% train_model_synthetic.py

if errorlevel 1 (
    echo.
    echo ❌ Training failed
    pause
    exit /b 1
)

echo.
echo ════════════════════════════════════════════════════════════════
echo ✅ MODEL TRAINING COMPLETE
echo ════════════════════════════════════════════════════════════════
echo.
echo 📊 Next Steps:
echo   1. Check xgboost_model.pkl was created
echo   2. Share model with backend person
echo   3. Backend deploys Flask app
echo   4. Frontend connects to API
echo.
pause
