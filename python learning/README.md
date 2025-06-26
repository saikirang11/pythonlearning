# 🐍 Python Learning Platform

A comprehensive full-stack Python learning platform with interactive lessons, quizzes, code execution, and AI-powered features.

## ✨ Features

### 🎓 Learning Features
- **Interactive Lessons** with syntax-highlighted code
- **AI-Generated Images** for visual learning
- **Embedded YouTube Videos** for multimedia content
- **PDF Text Extraction** from uploaded documents
- **In-Browser Code Execution** using Pyodide
- **Progress Tracking** with streaks and activity history
- **Bookmark & Resume** functionality

### 🧪 Quiz System
- **Interactive Quizzes** with instant feedback
- **Multiple Choice Questions** with explanations
- **Score Tracking** and performance analytics
- **Randomized Questions** for varied learning

### 👥 Community Features
- **Discussion Boards** under each lesson
- **User Comments** and interactions
- **Progress Sharing** and achievements

### 🔧 Admin Features
- **Lesson Management** with rich content editor
- **Quiz Creation** with multiple question types
- **File Upload** (PDFs, images, videos)
- **Analytics Dashboard** with user insights
- **AI Image Generation** for lesson visuals
- **Sample Data Seeding** for quick setup

### 🎨 User Experience
- **Dark/Light Mode** toggle
- **Internationalization** support (i18n)
- **Responsive Design** for all devices
- **Modern UI** with TailwindCSS
- **Real-time Updates** and notifications

## 🚀 Quick Start

### Option 1: Automated Setup (Windows)
```bash
# Double-click the start_platform.bat file
# Or run from command line:
start_platform.bat
```

### Option 2: Manual Setup

#### 1. Prerequisites
- Python 3.8+
- Node.js 16+
- MySQL 8.0+

#### 2. Environment Setup
```bash
# Create .env file
cp .env.example .env
# Edit .env with your database credentials
```

#### 3. Database Setup
```sql
CREATE DATABASE python_learning;
mysql -u your_user -p python_learning < mysql_schema.sql
```

#### 4. Install Dependencies
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

#### 5. Run the Application
```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

#### 6. Access the Platform
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## 📁 Project Structure

```
python learning/
├── backend/                 # Flask backend
│   ├── app.py              # Main application
│   ├── config.py           # Configuration
│   ├── models.py           # Database models
│   ├── routes/             # API routes
│   │   ├── auth.py         # Authentication
│   │   ├── lessons.py      # Lesson management
│   │   ├── quiz.py         # Quiz system
│   │   └── admin.py        # Admin features
│   ├── utils/              # Utility functions
│   │   ├── pdf_extractor.py # PDF text extraction
│   │   ├── image_generator.py # AI image generation
│   │   └── jwt_utils.py    # JWT authentication
│   ├── sample_data.py      # Sample lessons and quizzes
│   ├── python_roadmap.py   # Learning roadmap
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── pages/          # React components
│   │   │   ├── Dashboard.jsx
│   │   │   ├── LessonPage.jsx
│   │   │   ├── Login.jsx
│   │   │   └── ...
│   │   ├── App.jsx         # Main app component
│   │   ├── main.jsx        # Entry point
│   │   └── index.css       # Styles
│   ├── package.json        # Node.js dependencies
│   └── vite.config.js      # Build configuration
├── mysql_schema.sql        # Database schema
├── .env                    # Environment variables
├── start_platform.bat      # Windows startup script
├── quick_start.py          # Python setup script
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables (.env)
```env
# Database
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_DB=python_learning

# Flask
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret

# File Uploads
UPLOAD_FOLDER=uploads

# OpenAI (optional)
OPENAI_API_KEY=your-openai-key

# CORS
CORS_ORIGINS=http://localhost:3000
```

## 📚 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login

### Lessons
- `GET /api/v1/lessons` - Get all lessons
- `GET /api/v1/lesson/<id>` - Get specific lesson
- `GET /api/v1/progress` - Get user progress
- `GET /api/v1/roadmap` - Get learning roadmap

### Quizzes
- `GET /api/v1/quiz/<lesson_id>` - Get lesson quizzes
- `POST /api/v1/quiz/submit` - Submit quiz answers

### Discussions
- `GET /api/v1/lesson/<id>/discussions` - Get lesson discussions
- `POST /api/v1/lesson/<id>/discussions` - Post comment

### Admin (Admin only)
- `POST /api/v1/admin/lesson` - Create lesson
- `POST /api/v1/admin/upload-pdf` - Upload PDF
- `POST /api/v1/admin/seed-data` - Seed sample data
- `GET /api/v1/admin/analytics` - Get analytics

## 🎯 Usage Guide

### For Students
1. **Register/Login** - Create an account or sign in
2. **Browse Lessons** - Explore available Python lessons
3. **Take Quizzes** - Test your knowledge with interactive quizzes
4. **Track Progress** - Monitor your learning journey
5. **Join Discussions** - Participate in lesson discussions
6. **Run Code** - Execute Python code directly in the browser

### For Admins
1. **Access Admin Dashboard** - Manage platform content
2. **Create Lessons** - Add new learning materials
3. **Upload Content** - Add PDFs, images, and videos
4. **Generate AI Images** - Create visual content automatically
5. **View Analytics** - Monitor user engagement and progress
6. **Seed Sample Data** - Populate platform with example content

## 🛠️ Development

### Adding New Features

#### Backend
```bash
cd backend
# Modify files in routes/, models/, utils/
# Restart server: python app.py
```

#### Frontend
```bash
cd frontend
# Modify files in src/
# Auto-reloads on save
```

### Database Changes
```bash
# Modify models.py
# Update mysql_schema.sql if needed
# Restart backend
```

## 🚀 Deployment

### Replit Deployment
1. Upload files to Replit
2. Set environment variables in Replit secrets
3. Run `bash run.sh`

### Other Platforms
1. Build frontend: `npm run build`
2. Set up production database
3. Configure environment variables
4. Use production WSGI server

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Error
- Check MySQL is running
- Verify credentials in `.env`
- Ensure database exists

#### Module Not Found
```bash
cd backend
pip install -r requirements.txt
```

#### Frontend Build Error
```bash
cd frontend
npm install
```

#### CORS Error
- Check CORS_ORIGINS in `.env`
- Restart both servers

### Getting Help
1. Check the troubleshooting section in `STEP_BY_STEP_GUIDE.md`
2. Verify all prerequisites are installed
3. Check console logs for error messages
4. Ensure environment variables are correct

## 📈 Roadmap

### Planned Features
- [ ] Advanced analytics dashboard
- [ ] Gamification (badges, achievements)
- [ ] Social learning features
- [ ] Mobile app
- [ ] Offline mode
- [ ] Multi-language support
- [ ] Advanced code editor
- [ ] Real-time collaboration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Flask for the backend framework
- React for the frontend framework
- TailwindCSS for styling
- Pyodide for in-browser Python execution
- OpenAI for AI image generation

---

**Happy Learning! 🐍✨**

For detailed setup instructions, see `STEP_BY_STEP_GUIDE.md`
For environment setup, see `ENV_SETUP.md` 