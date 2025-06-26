from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Lesson, Progress, User, Discussion
from datetime import datetime, timedelta
from python_roadmap import PYTHON_ROADMAP

lessons_bp = Blueprint('lessons', __name__)

@lessons_bp.route('/lessons', methods=['GET'])
@jwt_required()
def get_lessons():
    # AI-powered search stub
    keyword = request.args.get('q')
    if keyword:
        # TODO: Integrate AI search
        lessons = Lesson.query.filter(Lesson.title.like(f'%{keyword}%')).all()
    else:
        lessons = Lesson.query.all()
    return jsonify([{
        'id': l.id,
        'title': l.title,
        'image_path': l.image_path,
        'video_url': l.video_url,
        'snippet': (l.content[:120] + '...') if l.content and len(l.content) > 120 else l.content
    } for l in lessons]), 200

@lessons_bp.route('/lesson/<int:lesson_id>', methods=['GET'])
@jwt_required()
def get_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    return jsonify({
        'id': lesson.id,
        'title': lesson.title,
        'content': lesson.content,
        'notes': lesson.notes,
        'code': lesson.code,
        'image_path': lesson.image_path,
        'video_url': lesson.video_url,
        'pdf_path': lesson.pdf_path
    }), 200

@lessons_bp.route('/progress', methods=['GET'])
@jwt_required()
def get_progress():
    identity = get_jwt_identity()
    user_id = identity['id']
    # Recent activity: last 5 lessons accessed
    recent = (
        db.session.query(Progress, Lesson)
        .join(Lesson, Progress.lesson_id == Lesson.id)
        .filter(Progress.user_id == user_id)
        .order_by(Progress.last_accessed.desc())
        .limit(5)
        .all()
    )
    recent_list = [
        {
            'id': l.id,
            'title': l.title,
            'date': p.last_accessed.strftime('%Y-%m-%d')
        }
        for p, l in recent
    ]
    # Streak: count consecutive days with activity
    progresses = (
        db.session.query(Progress)
        .filter(Progress.user_id == user_id)
        .order_by(Progress.last_accessed.desc())
        .all()
    )
    streak = 0
    today = datetime.utcnow().date()
    days = set(p.last_accessed.date() for p in progresses)
    for i in range(0, 100):
        day = today - timedelta(days=i)
        if day in days:
            streak += 1
        else:
            break
    return jsonify({'recent': recent_list, 'streak': streak}), 200

@lessons_bp.route('/lesson/<int:lesson_id>/discussions', methods=['GET'])
@jwt_required()
def get_discussions(lesson_id):
    discussions = (
        db.session.query(Discussion, User)
        .join(User, Discussion.user_id == User.id)
        .filter(Discussion.lesson_id == lesson_id)
        .order_by(Discussion.created_at.desc())
        .all()
    )
    return jsonify([
        {
            'id': d.id,
            'message': d.message,
            'username': u.username,
            'created_at': d.created_at.strftime('%Y-%m-%d %H:%M')
        }
        for d, u in discussions
    ]), 200

@lessons_bp.route('/lesson/<int:lesson_id>/discussions', methods=['POST'])
@jwt_required()
def post_discussion(lesson_id):
    identity = get_jwt_identity()
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'msg': 'Message is required'}), 400
    discussion = Discussion(
        lesson_id=lesson_id,
        user_id=identity['id'],
        message=message
    )
    db.session.add(discussion)
    db.session.commit()
    return jsonify({'msg': 'Comment posted successfully'}), 201

@lessons_bp.route('/roadmap', methods=['GET'])
def get_roadmap():
    return jsonify(PYTHON_ROADMAP), 200 