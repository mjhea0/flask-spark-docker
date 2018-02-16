# services/web/server/__init__.py


import os

from flask import Flask


app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)


app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


from server.main.views import main_blueprint
app.register_blueprint(main_blueprint)
