from flask import Flask
# from project.admin.routes import admin

app = Flask(__name__, template_folder="templates")

# app.register_blueprint(main, url_prefix='/')
# app.register_blueprint(admin, url_prefix='/admin')