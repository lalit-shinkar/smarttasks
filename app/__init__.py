from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes.views import main_routes
    app.register_blueprint(main_routes)

    return app

