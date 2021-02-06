from flask import Flask

from . import config

def create_app():
    from . import models, schemas
    app = Flask(__name__)
    models.init_app(app, config)
    schemas.init_app(app, config)
    return app

app = create_app()
if __name__ == "__main__":
    app.run(debug=getattr(config, 'debug'))