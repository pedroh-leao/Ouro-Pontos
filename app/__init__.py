from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.pontos_turisticos import bp as bp_pontos_turisticos
    app.register_blueprint(bp_pontos_turisticos)

    return app