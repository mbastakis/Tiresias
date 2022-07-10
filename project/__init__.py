from flask import Flask
# from project.admin.routes import admin
print('test0')
app = Flask(__name__)



# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# app.register_blueprint(main, url_prefix='/')
# app.register_blueprint(admin, url_prefix='/admin')