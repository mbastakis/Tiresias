from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return "Hello, World! This is the main page."