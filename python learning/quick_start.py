#!/usr/bin/env python3
"""
Quick Start Script for Python Learning Platform
This script helps you set up the environment and run the application.
"""

import os
import sys
import subprocess
import platform

def print_step(step_num, description):
    print(f"\n{'='*50}")
    print(f"STEP {step_num}: {description}")
    print(f"{'='*50}")

def run_command(command, description):
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        return False

def check_file_exists(filepath):
    return os.path.exists(filepath)

def main():
    print("🐍 Python Learning Platform - Quick Start")
    print("This script will help you set up and run the application.")
    
    # Step 1: Check if .env file exists
    print_step(1, "Environment Configuration")
    if not check_file_exists('.env'):
        print("❌ .env file not found!")
        print("Please create a .env file with the following content:")
        print("""
# Database Configuration
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_DB=python_learning

# Flask Configuration
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here

# File Upload Configuration
UPLOAD_FOLDER=uploads

# OpenAI Configuration (for AI image generation)
OPENAI_API_KEY=your-openai-api-key

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
        """)
        return
    else:
        print("✅ .env file found")

    # Step 2: Install Python dependencies
    print_step(2, "Installing Python Dependencies")
    if not run_command("cd backend && pip install -r requirements.txt", "Installing Python packages"):
        return

    # Step 3: Check if Node.js is installed
    print_step(3, "Checking Node.js Installation")
    if not run_command("node --version", "Checking Node.js"):
        print("❌ Node.js not found! Please install Node.js from https://nodejs.org/")
        return

    # Step 4: Install frontend dependencies
    print_step(4, "Installing Frontend Dependencies")
    if not run_command("cd frontend && npm install", "Installing npm packages"):
        return

    # Step 5: Create uploads directory
    print_step(5, "Creating Uploads Directory")
    os.makedirs("backend/uploads", exist_ok=True)
    print("✅ Uploads directory created")

    print_step(6, "Setup Complete!")
    print("""
🎉 Setup completed successfully!

Next steps:
1. Make sure MySQL is running and the database is created
2. Update your .env file with correct database credentials
3. Run the backend: cd backend && python app.py
4. Run the frontend: cd frontend && npm run dev
5. Open http://localhost:3000 in your browser

For detailed instructions, see ENV_SETUP.md
    """)

if __name__ == "__main__":
    main() 