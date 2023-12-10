import logging
import time

import connexion
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware


def setup_app(schema_path, session=None, fake_delay=0):
    logging.basicConfig(level=logging.INFO)

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
        if session:
            session.remove()

    @application.before_request
    def add_fake_delay():
        if fake_delay > 0:
            time.sleep(fake_delay)

    return app
