from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #init app
    db.init_app(app) #init db
    
    # check why and how this works (if the import is moved up it breaks for some reason)
    from ofertas import ofertas_bp
    app.register_blueprint(ofertas_bp)
    
    return app

# to run from here -> set FLASK_APP=APP -> python app.py (in bash)
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
