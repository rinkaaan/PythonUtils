import logging

import connexion
from connexion.middleware import MiddlewarePosition
from flask.cli import load_dotenv
from starlette.middleware.cors import CORSMiddleware

from nguylinc_python_utils.sqlalchemy import init_db


def setup_app(base, schema_path):
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    session = init_db(base)

    origins = ["http://localhost:5173", "https://lincolnnguyen.me"]

    app = connexion.FlaskApp(__name__)
    app.add_api(schema_path, validate_responses=True, strict_validation=True)
    app.add_middleware(
        CORSMiddleware,
        position=MiddlewarePosition.BEFORE_ROUTING,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application = app.app

    @application.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()

    return app, session
