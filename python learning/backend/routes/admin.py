from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Lesson, Analytics, Quiz
from utils.pdf_extractor import extract_text_from_pdf
from utils.image_generator import generate_explanation_image
from sample_data import SAMPLE_LESSONS, SAMPLE_QUIZZES
import os

admin_bp = Blueprint('admin', __name__)

# Helper to check admin
from functools import wraps
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        identity = get_jwt_identity()
        if not identity or not identity.get('is_admin'):
            return jsonify({'msg': 'Admin only'}), 403
        return fn(*args, **kwargs)
    return wrapper

@admin_bp.route('/upload-pdf', methods=['POST'])
@jwt_required()
@admin_required
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'msg': 'No PDF uploaded'}), 400
    pdf = request.files['pdf']
    filename = pdf.filename
    if not filename:
        return jsonify({'msg': 'Invalid filename'}), 400
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    pdf_path = os.path.join(upload_folder, filename)
    pdf.save(pdf_path)
    text = extract_text_from_pdf(pdf_path)
    return jsonify({'pdf_path': pdf_path, 'extracted_text': text}), 200

@admin_bp.route('/lesson', methods=['POST'])
@jwt_required()
@admin_required
def create_lesson():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    notes = data.get('notes')
    code = data.get('code')
    video_url = data.get('video_url')
    pdf_path = data.get('pdf_path')
    
    if not title or not content:
        return jsonify({'msg': 'Title and content are required'}), 400
    
    prompt = data.get('image_prompt', content)
    image_filename = f"{title.replace(' ', '_')}_explanation.png"
    image_path = generate_explanation_image(prompt, image_filename)
    
    lesson = Lesson(
        title=title,
        content=content,
        notes=notes,
        code=code,
        image_path=image_path,
        video_url=video_url,
        pdf_path=pdf_path,
        created_by=get_jwt_identity()['id']
    )
    db.session.add(lesson)
    db.session.commit()
    return jsonify({'msg': 'Lesson created', 'lesson_id': lesson.id}), 201

@admin_bp.route('/upload-image', methods=['POST'])
@jwt_required()
@admin_required
def upload_image():
    if 'image' not in request.files:
        return jsonify({'msg': 'No image uploaded'}), 400
    image = request.files['image']
    filename = image.filename
    if not filename:
        return jsonify({'msg': 'Invalid filename'}), 400
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, filename)
    image.save(image_path)
    return jsonify({'image_path': image_path}), 200

@admin_bp.route('/upload-video', methods=['POST'])
@jwt_required()
@admin_required
def upload_video():
    if 'video' not in request.files:
        return jsonify({'msg': 'No video uploaded'}), 400
    video = request.files['video']
    filename = video.filename
    if not filename:
        return jsonify({'msg': 'Invalid filename'}), 400
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    video_path = os.path.join(upload_folder, filename)
    video.save(video_path)
    return jsonify({'video_path': video_path}), 200

@admin_bp.route('/analytics', methods=['GET'])
@jwt_required()
@admin_required
def get_analytics():
    analytics = Analytics.query.all()
    return jsonify([
        {
            'lesson_id': a.lesson_id,
            'views': a.views,
            'quiz_attempts': a.quiz_attempts
        } for a in analytics
    ]), 200

@admin_bp.route('/seed-data', methods=['POST'])
@jwt_required()
@admin_required
def seed_data():
    try:
        user_id = get_jwt_identity()['id']
        created_lessons = []
        
        for i, lesson_data in enumerate(SAMPLE_LESSONS, 1):
            # Generate AI image for the lesson
            image_filename = f"lesson_{i}_explanation.png"
            image_path = generate_explanation_image(lesson_data['image_prompt'], image_filename)
            
            # Create lesson
            lesson = Lesson(
                title=lesson_data['title'],
                content=lesson_data['content'],
                notes=lesson_data['notes'],
                code=lesson_data['code'],
                image_path=image_path,
                video_url=lesson_data['video_url'],
                created_by=user_id
            )
            db.session.add(lesson)
            db.session.flush()  # Get the lesson ID
            
            # Add quizzes for this lesson
            if i in SAMPLE_QUIZZES:
                for quiz_data in SAMPLE_QUIZZES[i]:
                    quiz = Quiz(
                        lesson_id=lesson.id,
                        question=quiz_data['question'],
                        options=quiz_data['options'],
                        answer=quiz_data['answer'],
                        explanation=quiz_data['explanation']
                    )
                    db.session.add(quiz)
            
            created_lessons.append(lesson.title)
        
        db.session.commit()
        return jsonify({
            'msg': f'Successfully created {len(created_lessons)} sample lessons',
            'lessons': created_lessons
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': f'Failed to seed data: {str(e)}'}), 500 