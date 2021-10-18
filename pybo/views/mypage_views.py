from flask import Blueprint, render_template, session,redirect

bp = Blueprint('myPage', __name__, template_folder='templates', url_prefix='/mypage')
# 여기서 main 은 url_for 함수에 사용된다.

@bp.route('/')
def index():
    return render_template('mypage.html')