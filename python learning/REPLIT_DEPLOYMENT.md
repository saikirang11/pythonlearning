# 🚀 Replit Deployment Guide

## Prerequisites

Before deploying to Replit, make sure you have:
- A Replit account (free at [replit.com](https://replit.com))
- Basic knowledge of Replit's interface

## Step 1: Create New Replit

### 1.1 Create Project
1. Go to [replit.com](https://replit.com) and sign in
2. Click **"Create Repl"**
3. Choose **"Import from GitHub"**
4. Enter your repository URL or upload the project files
5. Select **"Python"** as the language
6. Click **"Create Repl"**

### 1.2 Alternative: Manual Upload
If you don't have a GitHub repository:
1. Create a new **Python** repl
2. Upload all project files manually
3. Or copy-paste the code files

## Step 2: Configure Replit Environment

### 2.1 Set Up Secrets (Environment Variables)
1. In your Replit, click on **"Tools"** in the left sidebar
2. Click **"Secrets"**
3. Add the following secrets:

```env
# Database Configuration
MYSQL_USER=your_replit_mysql_user
MYSQL_PASSWORD=your_replit_mysql_password
MYSQL_HOST=your_replit_mysql_host
MYSQL_DB=python_learning

# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this
JWT_SECRET_KEY=your-jwt-secret-key-change-this

# File Upload Configuration
UPLOAD_FOLDER=uploads

# OpenAI Configuration (optional)
OPENAI_API_KEY=your-openai-api-key

# CORS Configuration
CORS_ORIGINS=https://your-repl-name.your-username.repl.co
```

### 2.2 Set Up Replit Database
1. Click on **"Tools"** → **"Database"**
2. Choose **"MySQL"** or **"PostgreSQL"**
3. Note down the connection details
4. Update your secrets with the database credentials

## Step 3: Configure Project Files

### 3.1 Update .replit File
Make sure your `.replit` file is configured correctly:

```toml
language = "python3"
run = "bash run.sh"
entrypoint = "run.sh"

[nix]
channel = "stable-22_11"

[env]
PYTHONPATH = "${PYTHONPATH}:${REPL_HOME}"

[packager]
language = "python3"
ignoredPackages = ["unit_tests"]

[packager.features]
packageSearch = true
guessImports = true

[languages.python3]
pattern = "**/*.py"
syntax = "python"

[languages.javascript]
pattern = "**/*.{js,jsx,ts,tsx}"
syntax = "javascript"

[languages.css]
pattern = "**/*.css"
syntax = "css"

[languages.html]
pattern = "**/*.html"
syntax = "html"
```

### 3.2 Update run.sh Script
Ensure your `run.sh` script is executable and contains:

```bash
#!/bin/bash

echo "🐍 Python Learning Platform - Replit Deployment"
echo "================================================"

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r backend/requirements.txt

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
cd frontend
npm install
cd ..

# Create uploads directory
echo "Creating uploads directory..."
mkdir -p backend/uploads

# Set up database (if using Replit's built-in database)
echo "Setting up database..."
# You can add database initialization here if needed

# Start the application
echo "Starting the application..."
echo "Backend will run on port 5000"
echo "Frontend will run on port 3000"
echo ""

# Start backend in background
cd backend
python app.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
cd ../frontend
npm run dev &
FRONTEND_PID=$!

# Keep the script running
echo "Application started successfully!"
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "🌐 Your application will be available at:"
echo "   https://your-repl-name.your-username.repl.co"
echo ""
echo "Press Ctrl+C to stop the application"

# Wait for user to stop
wait
```

### 3.3 Update replit.nix
Make sure your `replit.nix` file includes all necessary packages:

```nix
{ pkgs }: {
  deps = [
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.nodejs-18_x
    pkgs.nodePackages.npm
    pkgs.mysql80
    pkgs.git
    pkgs.wget
    pkgs.curl
  ];
}
```

## Step 4: Database Setup

### 4.1 Using Replit's Built-in Database
1. Go to **"Tools"** → **"Database"**
2. Choose **"MySQL"** or **"PostgreSQL"**
3. Copy the connection string
4. Update your secrets with the database credentials

### 4.2 Using External Database
1. Use a service like **PlanetScale**, **Railway**, or **Supabase**
2. Get the connection details
3. Update your secrets accordingly

### 4.3 Initialize Database Schema
1. In the Replit shell, run:
```bash
# If using MySQL
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DB < mysql_schema.sql

# Or manually create tables using the schema
```

## Step 5: Deploy and Run

### 5.1 Start the Application
1. Click the **"Run"** button in Replit
2. Wait for the setup to complete
3. Check the console for any errors

### 5.2 Access Your Application
- Your app will be available at: `https://your-repl-name.your-username.repl.co`
- The backend API will be at: `https://your-repl-name.your-username.repl.co/api`

## Step 6: Initial Setup

### 6.1 Register Admin User
1. Go to your deployed application
2. Click **"Register"**
3. Create an admin account
4. Login with your credentials

### 6.2 Seed Sample Data
1. Go to **Admin Dashboard**
2. Click **"Seed Sample Data"**
3. This will populate the platform with sample lessons

## Step 7: Configuration Updates

### 7.1 Update CORS Settings
In your `.env` secrets, make sure CORS_ORIGINS includes your Replit URL:
```env
CORS_ORIGINS=https://your-repl-name.your-username.repl.co
```

### 7.2 Update Frontend API Base URL
If needed, update the frontend to use the correct API URL:
```javascript
// In frontend/src/App.jsx or similar
const API_BASE = 'https://your-repl-name.your-username.repl.co/api';
```

## Troubleshooting

### Common Issues:

#### 1. Database Connection Error
```
Error: Can't connect to MySQL server
```
**Solutions:**
- Check database credentials in secrets
- Ensure database service is running
- Try using Replit's built-in database

#### 2. Port Issues
```
Error: Port already in use
```
**Solutions:**
- Replit automatically handles port forwarding
- Make sure your app listens on `0.0.0.0:5000`

#### 3. Dependencies Not Found
```
ModuleNotFoundError: No module named 'flask'
```
**Solutions:**
- Check `requirements.txt` is in the correct location
- Ensure `run.sh` installs dependencies before starting

#### 4. Frontend Build Error
```
Error: Cannot find module 'react'
```
**Solutions:**
- Check `package.json` is in the frontend directory
- Ensure `npm install` runs before `npm run dev`

#### 5. CORS Error
```
Access to fetch has been blocked by CORS policy
```
**Solutions:**
- Update CORS_ORIGINS in secrets
- Include your Replit URL in the allowed origins

### Debugging Tips:

1. **Check Console Logs**: Look at the Replit console for error messages
2. **Test API Endpoints**: Use the Replit console to test API calls
3. **Check Secrets**: Verify all environment variables are set correctly
4. **Database Connection**: Test database connectivity manually

## Advanced Configuration

### Custom Domain (Replit Pro)
1. Go to **"Tools"** → **"Domains"**
2. Add your custom domain
3. Update CORS_ORIGINS to include your domain

### Environment-Specific Settings
Create different configurations for development and production:

```python
# In backend/config.py
import os

class Config:
    if os.getenv('REPL_ID'):  # Running on Replit
        SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    else:  # Local development
        SQLALCHEMY_DATABASE_URI = "mysql://localhost/python_learning"
```

### Performance Optimization
1. **Enable Caching**: Use Replit's caching features
2. **Optimize Images**: Compress uploaded images
3. **Database Indexing**: Add indexes for frequently queried fields

## Monitoring and Maintenance

### 1. Check Application Status
- Monitor the Replit console for errors
- Check database connections
- Verify API endpoints are responding

### 2. Update Dependencies
- Regularly update Python packages
- Keep Node.js dependencies current
- Monitor for security updates

### 3. Backup Data
- Export database regularly
- Backup uploaded files
- Keep configuration backups

## Success Checklist

- [ ] Replit project created successfully
- [ ] All environment variables set in secrets
- [ ] Database configured and connected
- [ ] Dependencies installed without errors
- [ ] Application starts without errors
- [ ] Frontend accessible at Replit URL
- [ ] Backend API responding correctly
- [ ] Admin user registered
- [ ] Sample data seeded
- [ ] All features working (lessons, quizzes, etc.)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review Replit's documentation
3. Check the console logs for specific errors
4. Verify all configuration steps are completed

---

**🎉 Your Python Learning Platform is now live on Replit!**

Visit your application and start learning Python! 🐍✨ 