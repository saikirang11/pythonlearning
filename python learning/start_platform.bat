@echo off
echo 🐍 Python Learning Platform - Quick Start
echo ========================================

echo.
echo Step 1: Checking environment...
if not exist ".env" (
    echo ❌ .env file not found!
    echo Please create a .env file with your configuration.
    echo See ENV_SETUP.md for details.
    pause
    exit /b 1
)

echo ✅ .env file found

echo.
echo Step 2: Installing Python dependencies...
cd backend
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install Python dependencies
    pause
    exit /b 1
)

echo.
echo Step 3: Installing Node.js dependencies...
cd ..\frontend
npm install
if %errorlevel% neq 0 (
    echo ❌ Failed to install Node.js dependencies
    pause
    exit /b 1
)

echo.
echo Step 4: Creating uploads directory...
cd ..\backend
if not exist "uploads" mkdir uploads

echo.
echo ✅ Setup completed successfully!
echo.
echo 🚀 Starting the application...
echo.
echo Backend will run on: http://localhost:5000
echo Frontend will run on: http://localhost:3000
echo.
echo Press Ctrl+C to stop both servers
echo.

cd ..
start "Backend Server" cmd /k "cd backend && python app.py"
timeout /t 3 /nobreak >nul
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo.
echo 🌐 Opening application in browser...
timeout /t 5 /nobreak >nul
start http://localhost:3000

echo.
echo 🎉 Application started successfully!
echo Keep both terminal windows open to run the application.
echo.
pause 