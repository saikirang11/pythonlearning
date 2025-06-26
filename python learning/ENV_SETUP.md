# Environment Setup Guide

## Step 1: Create Environment File

Create a `.env` file in the root directory with the following variables:

```env
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
```

## Step 2: Database Setup

1. Install MySQL if not already installed
2. Create a database named `python_learning`
3. Run the SQL schema: `mysql -u your_user -p python_learning < mysql_schema.sql`

## Step 3: Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## Step 4: Frontend Dependencies

```bash
cd frontend
npm install
```

## Step 5: Run the Application

### Terminal 1 - Backend:
```bash
cd backend
python app.py
```

### Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

## Step 6: Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Step 7: Seed Sample Data

1. Register an admin user
2. Login as admin
3. Go to Admin Dashboard
4. Click "Seed Sample Data" to populate lessons and quizzes 