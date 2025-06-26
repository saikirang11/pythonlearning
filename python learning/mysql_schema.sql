-- Python Learning Platform Database Schema
-- MySQL Database Schema for Python Learning Platform

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS python_learning;
USE python_learning;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Lessons table
CREATE TABLE IF NOT EXISTS lessons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    notes TEXT,
    code TEXT,
    image_path VARCHAR(255),
    video_url VARCHAR(255),
    pdf_path VARCHAR(255),
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);

-- Quizzes table
CREATE TABLE IF NOT EXISTS quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_id INT NOT NULL,
    question TEXT NOT NULL,
    options JSON NOT NULL,
    answer VARCHAR(255) NOT NULL,
    explanation TEXT,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id) ON DELETE CASCADE
);

-- Discussions table
CREATE TABLE IF NOT EXISTS discussions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_id INT NOT NULL,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Progress table
CREATE TABLE IF NOT EXISTS progress (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    lesson_id INT NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_lesson (user_id, lesson_id)
);

-- Analytics table
CREATE TABLE IF NOT EXISTS analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_id INT NOT NULL,
    views INT DEFAULT 0,
    quiz_attempts INT DEFAULT 0,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_lessons_created_by ON lessons(created_by);
CREATE INDEX idx_quizzes_lesson_id ON quizzes(lesson_id);
CREATE INDEX idx_discussions_lesson_id ON discussions(lesson_id);
CREATE INDEX idx_discussions_user_id ON discussions(user_id);
CREATE INDEX idx_progress_user_id ON progress(user_id);
CREATE INDEX idx_progress_lesson_id ON progress(lesson_id);
CREATE INDEX idx_analytics_lesson_id ON analytics(lesson_id);

-- Insert sample admin user (password: admin123)
INSERT INTO users (username, email, password_hash, is_admin) VALUES 
('admin', 'admin@pythonlearning.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.gS.OiG', TRUE)
ON DUPLICATE KEY UPDATE username=username;

-- Insert sample lessons
INSERT INTO lessons (title, content, notes, code, video_url, created_by) VALUES 
('Python Basics - Getting Started', 'Python is a high-level, interpreted programming language known for its simplicity and readability. It\'s perfect for beginners and widely used in web development, data science, artificial intelligence, and more. Let\'s start with the fundamentals!', 'Python uses dynamic typing - you don\'t need to declare variable types. Indentation is crucial for code blocks. Use meaningful variable names and comments to make your code readable.', '# Your first Python program\nprint(\'Hello, World!\')\n\n# Variables and basic data types\nname = \'Alice\'          # String\nage = 25               # Integer\nheight = 5.9           # Float\nis_student = True      # Boolean\n\n# String formatting\nprint(f\'My name is {name} and I am {age} years old\')\nprint(\'Height:\', height, \'feet\')\nprint(\'Student status:\', is_student)\n\n# Basic operations\nx = 10\ny = 3\nprint(f\'Addition: {x + y}\')\nprint(f\'Subtraction: {x - y}\')\nprint(f\'Multiplication: {x * y}\')\nprint(f\'Division: {x / y}\')\nprint(f\'Floor division: {x // y}\')\nprint(f\'Modulus: {x % y}\')\nprint(f\'Power: {x ** y}\')', 'https://www.youtube.com/embed/rfscVS0vtbw', 1),
('Python Control Flow - Making Decisions', 'Control flow statements allow your program to make decisions and execute different code based on conditions. Python provides if, elif, and else statements for conditional execution, and various loop structures for repetitive tasks.', 'Python uses indentation (4 spaces) to define code blocks. The elif keyword is used for additional conditions, and else is used for the default case. Logical operators (and, or, not) help combine conditions.', '# If statements\nage = 18\n\nif age >= 18:\n    print(\'You are an adult\')\nelif age >= 13:\n    print(\'You are a teenager\')\nelse:\n    print(\'You are a child\')\n\n# Comparison operators\nx = 10\ny = 5\n\nprint(f\'x > y: {x > y}\')\nprint(f\'x < y: {x < y}\')\nprint(f\'x == y: {x == y}\')\nprint(f\'x != y: {x != y}\')\nprint(f\'x >= y: {x >= y}\')\nprint(f\'x <= y: {x <= y}\')\n\n# Logical operators\nis_student = True\nhas_id = True\n\nif is_student and has_id:\n    print(\'Student discount applied!\')\n\nif is_student or has_id:\n    print(\'Some benefits available\')\n\nif not is_student:\n    print(\'Regular pricing\')', 'https://www.youtube.com/embed/DZwmZ8Usvnk', 1)
ON DUPLICATE KEY UPDATE title=title;

-- Insert sample quizzes
INSERT INTO quizzes (lesson_id, question, options, answer, explanation) VALUES 
(1, 'What is the correct way to print "Hello, World!" in Python?', '["print(\'Hello, World!\')", "echo(\'Hello, World!\')", "console.log(\'Hello, World!\')", "printf(\'Hello, World!\')"]', 'print(\'Hello, World!\')', 'Python uses the print() function to output text to the console.'),
(1, 'Which of the following is a valid Python variable name?', '["2name", "my-name", "my_name", "class"]', 'my_name', 'Variable names can contain letters, numbers, and underscores, but cannot start with a number or contain hyphens.'),
(1, 'What is the result of 5 // 2 in Python?', '["2.5", "2", "2.0", "3"]', '2', 'The // operator performs floor division, which returns the largest integer less than or equal to the division result.'),
(2, 'What is the correct syntax for an if statement in Python?', '["if x > y:", "if (x > y)", "if x > y then", "if x > y {"]', 'if x > y:', 'Python uses colons (:) to indicate the start of a code block, not parentheses or braces.'),
(2, 'Which keyword is used for additional conditions in an if statement?', '["elseif", "elif", "else if", "ifelse"]', 'elif', 'elif is the Python keyword for "else if" - it allows you to check multiple conditions.')
ON DUPLICATE KEY UPDATE question=question;

-- Insert sample analytics
INSERT INTO analytics (lesson_id, views, quiz_attempts) VALUES 
(1, 0, 0),
(2, 0, 0)
ON DUPLICATE KEY UPDATE lesson_id=lesson_id; 