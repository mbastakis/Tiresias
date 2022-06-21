from flask import Blueprint

admin = Blueprint('admin', __name__)

@main.route('/')
def index():
	return "Hello, World! This is the admin page."