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

    @app.route('/test/', methods=["GET"])
    def test_page() -> str:
        return '<h3 style="text-align:center; color: green; margin-top:40px;">Testing the Flask Application Factory Pattern</h3>'

    return app

''' 
  While in your base directory with venv activated run these commands to tell Flask where the factory function is
  by passing the core application's directory name as 'app' as a value to the FLASK_APP enviromental variable.
  And then set your FLASK_ENV to development to take full use of the debugger.

    Setup FLASK_APP and FLASK_ENV:
      - set FLASK_APP=app
      - set FLASK_ENV=development
    or:
      - export FLASK_APP=app
      - export FLASK_ENV=development
    for Linux

'''
 