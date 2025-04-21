from flask import Flask
from backend.auth import auth
from backend.views import views
import os

def create_app():
    app = Flask(
        __name__, 
        template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."),
        static_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static")
    ) 
    app.config['SECRET_KEY'] = "h4?+Do^^XZVsxr^uT*g;6=8C*asvFj(/6Va;i=gZeI$Lvo!&fm;{f'^Zc:ZiuK|"

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)