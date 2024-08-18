from flask import Flask


def create_app():
    app = Flask(__name__)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.pontos_turisticos import bp as bp_pontos_turisticos
    app.register_blueprint(bp_pontos_turisticos)

    return app