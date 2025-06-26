# 🚀 Replit Deployment Guide

## Quick Start

### 1. Fork/Import to Replit
1. Go to [replit.com](https://replit.com)
2. Click "Create Repl"
3. Choose "Import from GitHub" or fork this repository
4. Select "Python" as the language

### 2. Set Up Environment Variables
In Replit, go to **Secrets** (lock icon) and add:

```env
FLASK_ENV=development
SECRET_KEY=your_super_secret_key_here_make_it_long_and_random
JWT_SECRET_KEY=your_jwt_secret_key_here_also_long_and_random
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=python_learning
OPENAI_API_KEY=your_openai_api_key_here
UPLOAD_FOLDER=uploads
CORS_ORIGINS=*
```

### 3. Set Up MySQL Database
1. In Replit, go to **Tools** → **Database**
2. Create a new MySQL database
3. Copy the connection details to your secrets
4. Import the `mysql_schema.sql` file

### 4. Install Dependencies
Run these commands in the Replit shell:

```bash
# Make run script executable
chmod +x run.sh

# Install Python dependencies
cd backend
pip install -r requirements.txt

# Install Node.js dependencies
cd ../frontend
npm install
```

### 5. Start the Application
Run the deployment script:

```bash
./run.sh
```

Or manually start both services:

```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## 🔧 Configuration

### Backend Configuration
- **Port**: 5000 (default)
- **Database**: MySQL
- **File Uploads**: `/backend/uploads/`
- **CORS**: Enabled for frontend

### Frontend Configuration
- **Port**: 5173 (Vite default)
- **API Base URL**: `http://localhost:5000/api/v1/`
- **Build Tool**: Vite

## 📝 Initial Setup

### 1. Register a User
1. Go to your Replit URL
2. Click "Register"
3. Create your first user account

### 2. Set Up Admin Access
1. In your MySQL database, run:
```sql
UPDATE users SET is_admin = TRUE WHERE username = 'your_username';
```

### 3. Seed Sample Data
1. Login as admin
2. Go to Admin Dashboard
3. Click "Seed Sample Data"
4. Wait for AI images to generate

## 🌐 Accessing Your Platform

### Development Mode
- **Frontend**: `https://your-repl-name.your-username.repl.co`
- **Backend API**: `https://your-repl-name.your-username.repl.co:5000`

### Production Mode
- **Main URL**: `https://your-repl-name.your-username.repl.co`

## 🔍 Troubleshooting

### Common Issues

#### 1. Database Connection Error
```
Error: Can't connect to MySQL server
```
**Solution**: 
- Check MySQL is running in Replit
- Verify database credentials in Secrets
- Ensure database exists

#### 2. Module Not Found
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**:
```bash
cd backend
pip install -r requirements.txt
```

#### 3. Frontend Build Error
```
Error: Cannot find module 'react'
```
**Solution**:
```bash
cd frontend
npm install
```

#### 4. OpenAI API Error
```
Error: Invalid API key
```
**Solution**:
- Check your OpenAI API key in Secrets
- Ensure you have credits in your OpenAI account

#### 5. File Upload Issues
```
Error: Upload folder not found
```
**Solution**:
```bash
mkdir -p backend/uploads
chmod 755 backend/uploads
```

### Performance Tips

1. **Use Replit's MySQL**: Faster than external databases
2. **Optimize Images**: Compress uploaded images
3. **Cache Static Files**: Use CDN for production
4. **Monitor Resources**: Check Replit's resource usage

## 🔒 Security Considerations

1. **Strong Secrets**: Use long, random strings for SECRET_KEY and JWT_SECRET_KEY
2. **API Keys**: Never commit API keys to code
3. **Database**: Use strong passwords for MySQL
4. **CORS**: Configure CORS_ORIGINS properly for production

## 📊 Monitoring

### Check Application Status
```bash
# Check if backend is running
curl http://localhost:5000/api/v1/lessons

# Check if frontend is running
curl http://localhost:5173
```

### View Logs
- Backend logs appear in the Replit console
- Frontend logs appear in browser developer tools

## 🚀 Production Deployment

### 1. Build Frontend
```bash
cd frontend
npm run build
```

### 2. Configure Production Settings
Update `backend/config.py`:
```python
class ProductionConfig(Config):
    DEBUG = False
    CORS_ORIGINS = "https://your-domain.com"
```

### 3. Set Up Domain (Optional)
- Configure custom domain in Replit
- Update CORS settings
- Set up SSL certificates

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review Replit's documentation
3. Check the application logs
4. Verify all environment variables are set

## 🎉 Success!

Once deployed, your Python Learning Platform will be accessible at:
`https://your-repl-name.your-username.repl.co`

Students can:
- Register and login
- Access the Python Roadmap
- Take interactive lessons
- Run code in the browser
- Take quizzes and track progress
- Participate in discussions

Admins can:
- Upload new lessons
- Generate AI images
- View analytics
- Manage content

Happy coding! 🐍✨ 