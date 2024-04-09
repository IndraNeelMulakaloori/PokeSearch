from flask import  Flask
from .routes import main

def create_app():
    # port = process.env.PORT or 4000
    app = Flask(__name__, template_folder='templates')

    app.register_blueprint(main)

    return app


# if __name__ == '__main__':
#     app = create_app()
#     app.run(port = 8000,debug=True)

    
