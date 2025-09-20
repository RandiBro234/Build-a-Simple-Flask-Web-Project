from flask import Flask
from board import pages

def create_app():
    app = Flask(__name__)
<<<<<<< HEAD
=======

>>>>>>> a6a3d88 (Initial commit project Flask message board)
    app.register_blueprint(pages.bp)
    return app
