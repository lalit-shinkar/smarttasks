from app.backend.models import db
from app.backend.controllers import api_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.views import main_routes
    app.register_blueprint(main_routes)

    app.register_blueprint(api_routes)

    with app.app_context():
        db.create_all()

    return app


