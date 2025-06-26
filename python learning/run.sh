#!/bin/bash

echo "🚀 Starting Python Learning Platform on Replit..."

# Create uploads directory if it doesn't exist
mkdir -p backend/uploads

# Install Python dependencies
echo "📦 Installing Python dependencies..."
cd backend
pip install -r requirements.txt

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
cd ../frontend
npm install

# Start the backend server
echo "🔧 Starting backend server..."
cd ../backend
python app.py &

# Wait a moment for backend to start
sleep 3

# Start the frontend development server
echo "🎨 Starting frontend server..."
cd ../frontend
npm run dev &

echo "✅ Python Learning Platform is starting up!"
echo "🌐 Backend: http://localhost:5000"
echo "🎨 Frontend: http://localhost:5173"
echo ""
echo "📝 Next steps:"
echo "1. Set up your environment variables in Replit Secrets"
echo "2. Configure your MySQL database"
echo "3. Register a user and set up admin access"
echo "4. Use 'Seed Sample Data' in the admin dashboard"

# Keep the script running
wait 