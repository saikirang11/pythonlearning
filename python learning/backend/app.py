from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager
from config import Config
import os

db = SQLAlchemy()
jwt = JWTManager()

limiter = Limiter(key_func=get_remote_address)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=Config.CORS_ORIGINS, supports_credentials=True)
    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)

    # Register blueprints (to be implemented)
    from routes.auth import auth_bp
    from routes.lessons import lessons_bp
    from routes.quiz import quiz_bp
    from routes.admin import admin_bp
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(lessons_bp, url_prefix='/api/v1')
    app.register_blueprint(quiz_bp, url_prefix='/api/v1')
    app.register_blueprint(admin_bp, url_prefix='/api/v1/admin')

    # Serve uploads
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000) 