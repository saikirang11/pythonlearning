# 🐍 Python Learning Platform - Step by Step Guide

## Prerequisites

Before starting, make sure you have:
- Python 3.8+ installed
- Node.js 16+ installed
- MySQL 8.0+ installed and running
- Git (optional, for version control)

## Step 1: Environment Setup

### 1.1 Create Environment File
Create a `.env` file in the root directory:

```bash
# In the root directory (python learning/)
touch .env
```

Add the following content to `.env`:

```env
# Database Configuration
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_DB=python_learning

# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this
JWT_SECRET_KEY=your-jwt-secret-key-change-this

# File Upload Configuration
UPLOAD_FOLDER=uploads

# OpenAI Configuration (optional - for AI image generation)
OPENAI_API_KEY=your-openai-api-key

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 1.2 Database Setup
1. **Start MySQL service**
2. **Create database:**
   ```sql
   CREATE DATABASE python_learning;
   ```
3. **Import schema:**
   ```bash
   mysql -u your_username -p python_learning < mysql_schema.sql
   ```

## Step 2: Backend Setup

### 2.1 Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2.2 Create Uploads Directory
```bash
mkdir uploads
```

### 2.3 Test Backend
```bash
python app.py
```

You should see: `Running on http://0.0.0.0:5000`

## Step 3: Frontend Setup

### 3.1 Install Node.js Dependencies
```bash
cd frontend
npm install
```

### 3.2 Test Frontend
```bash
npm run dev
```

You should see: `Local: http://localhost:3000/`

## Step 4: Running the Application

### 4.1 Start Backend (Terminal 1)
```bash
cd backend
python app.py
```

### 4.2 Start Frontend (Terminal 2)
```bash
cd frontend
npm run dev
```

### 4.3 Access the Application
- Open your browser and go to: `http://localhost:3000`
- The backend API will be available at: `http://localhost:5000`

## Step 5: Initial Setup

### 5.1 Register Admin User
1. Go to `http://localhost:3000/register`
2. Create an account with admin privileges
3. Login with your credentials

### 5.2 Seed Sample Data
1. Go to Admin Dashboard
2. Click "Seed Sample Data" button
3. This will create sample lessons and quizzes

## Step 6: Testing Features

### 6.1 Test Student Features
- Browse lessons
- Take quizzes
- View progress
- Use code runner
- Participate in discussions

### 6.2 Test Admin Features
- Upload new lessons
- Create quizzes
- View analytics
- Manage content

## Troubleshooting

### Common Issues:

#### 1. Database Connection Error
```
Error: Can't connect to MySQL server
```
**Solution:** 
- Check if MySQL is running
- Verify credentials in `.env` file
- Ensure database exists

#### 2. Module Not Found Error
```
ModuleNotFoundError: No module named 'flask'
```
**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

#### 3. Frontend Build Error
```
Error: Cannot find module 'react'
```
**Solution:**
```bash
cd frontend
npm install
```

#### 4. CORS Error
```
Access to fetch at 'http://localhost:5000' from origin 'http://localhost:3000' has been blocked by CORS policy
```
**Solution:**
- Check CORS_ORIGINS in `.env` file
- Restart both backend and frontend

#### 5. Port Already in Use
```
Error: listen EADDRINUSE: address already in use :::5000
```
**Solution:**
- Kill the process using the port
- Or change the port in the configuration

## Development Workflow

### Adding New Features:

1. **Backend Changes:**
   - Modify files in `backend/`
   - Restart backend server
   - Test API endpoints

2. **Frontend Changes:**
   - Modify files in `frontend/src/`
   - Frontend will auto-reload
   - Test in browser

3. **Database Changes:**
   - Modify `models.py`
   - Run database migrations
   - Update schema if needed

## Production Deployment

### For Replit:
1. Use the provided `run.sh` script
2. Set environment variables in Replit secrets
3. Configure database connection

### For Other Platforms:
1. Build frontend: `npm run build`
2. Set up production database
3. Configure environment variables
4. Use production WSGI server

## File Structure Overview

```
python learning/
├── backend/                 # Flask backend
│   ├── app.py              # Main application
│   ├── config.py           # Configuration
│   ├── models.py           # Database models
│   ├── routes/             # API routes
│   ├── utils/              # Utility functions
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── src/                # Source code
│   ├── package.json        # Node.js dependencies
│   └── vite.config.js      # Build configuration
├── mysql_schema.sql        # Database schema
├── .env                    # Environment variables
└── README.md              # Project documentation
```

## Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Verify all prerequisites are installed
3. Ensure environment variables are correct
4. Check console logs for error messages

## Next Steps

Once the platform is running:
1. Customize the content for your needs
2. Add more lessons and quizzes
3. Configure AI features (if using OpenAI)
4. Set up user authentication
5. Deploy to production

---

**Happy Learning! 🐍✨** 