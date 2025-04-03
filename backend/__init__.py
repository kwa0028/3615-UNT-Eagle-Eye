from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "h4?+Do^^XZVsxr^uT*g;6=8C*asvFj(/6Va;i=gZeI$Lvo!&fm;{f'^Zc:ZiuK|"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')

    return app