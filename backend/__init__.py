from flask import Flask
from auth import auth
from views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "h4?+Do^^XZVsxr^uT*g;6=8C*asvFj(/6Va;i=gZeI$Lvo!&fm;{f'^Zc:ZiuK|"

    app.register_blueprint(views)
    app.register_blueprint(auth)

    if __name__ == "__main__":
        app.run(debug=True)

    return app
