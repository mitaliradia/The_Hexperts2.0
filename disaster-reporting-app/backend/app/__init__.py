# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate(compare_type=True)
jwt = JWTManager()

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_object)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    # Import models after db initialization to avoid circular import
    from app.models.user import User
    from app.models.disaster import Disaster
    from app.models.log import Log

    return app
