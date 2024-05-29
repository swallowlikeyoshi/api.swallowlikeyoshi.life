from flask import Flask
from api.main import main as main_bp
from api.blog import blog as blog_bp

def create_app():
    app = Flask(__name__)
    
    # Blueprint 등록
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp, url_prefix='/blog')
    
    return app
