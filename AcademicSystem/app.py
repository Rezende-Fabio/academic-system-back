from flask import Flask
from AcademicSystem.extensions import Configuration
from AcademicSystem.extensions import Cors
from AcademicSystem.extensions import ResgisterBlueprint

def create_app():
    app = Flask(__name__) 
    Configuration.init_app(app)
    Cors.init_app(app)
    ResgisterBlueprint.resgister_blueprint(app)

    return app

if __name__ == '__main__':
    create_app().run()


