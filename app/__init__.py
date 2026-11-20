from pathlib import Path

from flask import Flask

from .database import init_db
from .routes.api import api
from .routes.web import web


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="local-development-key-change-before-deploying",
        DATABASE=str(Path(app.instance_path) / "luma_study.sqlite3"),
        MAX_CONTENT_LENGTH=2 * 1024 * 1024,
    )
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    init_db(app)
    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix="/api")

    @app.errorhandler(404)
    def not_found(_error):
        return "Page not found", 404

    @app.errorhandler(500)
    def server_error(_error):
        return {"error": "Something went wrong. Please try again."}, 500

    return app
