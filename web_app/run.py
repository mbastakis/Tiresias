#!/usr/bin/python3
from project import app
from project import routes

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
