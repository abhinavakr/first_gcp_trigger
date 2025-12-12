from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "replace-with-a-strong-secret-in-production"

    # Register blueprints / routes
    from .routes import bp
    app.register_blueprint(bp)

    return app