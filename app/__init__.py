from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import AppGroup
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)

    # Import and register the seed command
    seed_cli = AppGroup('seed')

    @seed_cli.command('all')
    def seed():
        from .seeds import seed_data
        seed_data()
        print("Seeding completed!")

    app.cli.add_command(seed_cli)

    return app
