# -*- coding: utf-8 -*-
from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')
#auth라는 URL 접두어로 시작하는 URL이 호출되면 auth_views.py 파일의 함수들이 호출될 수 있도록 블루프린트 추

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(student_id=form.student_id.data).first()
        if not user:
            user = User(student_id=form.student_id.data,
                        password=form.password1.data,
                        nickname=form.nickname.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login.login'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    d_time = session.get('d_time')

    if user_id is None and d_time is None:  # user_id와 d_time에 데이터가 없는 경우
        g.user = None
    elif d_time is None:                    # d_time에 데이터가 없는 경우, user_id만 get
        g.user = User.query.get(user_id)
    elif user_id is None:                   # user_id에 데이터가 없는 경우, d_time만 get
        g.user=User.query.get(d_time)
    else:                                   # d_time, user_id 데이터가 있는 경우 모두 get
        g.user = User.query.get(user_id)
        g.user = User.query.get(d_time)
