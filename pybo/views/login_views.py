from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.utils import redirect

from pybo.forms import UserLoginForm
from pybo.models import User

bp = Blueprint('login', __name__, url_prefix='/login')


# @bp.route('/')
# def login():
#     return render_template('login.html')


@bp.route('/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(student_id=form.student_id.data).first()
        if not user:
            error = "존재하지 않는 계정입니다."
        elif not user.password == form.password.data:
            error = "비밀번호가 올바르지 않습니다."
            print(user.password)
            print(form.password.data)
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('login.html', form=form)
