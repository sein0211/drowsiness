# -*- coding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # 플라스크 애플리케이션 생성.
    # __name__ : 모듈명. 여기서는 pybo라는 문자열이 담김
    # @app.route: 특정 주소에 접속하면 바로 다음줄의 함수를 호출
    app.config.from_object(config)
    # config.py에 작성한 항목을 app.config 환경 변수로 부름

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    # 전역변수로 db, migrate 객체를 만든 다음 init_app 메서드를 이용해 기초

    # 블루프린트
    from .views import main_views, login_views, auth_views, camera_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(login_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(camera_views.bp)
    # create_app 함수에 등록된 hello_pybo 함수 대신 블루프린트를 사용하도록 변경
    # 블루프린트를 사용하기 위해 main_views.py파일에서 생성한 블루프린트 객체 bp 등록

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    return app

# create_app 함수가 app 객체를 생성해 반환
# create_app 함수 = 애플리케이션 팩토리
