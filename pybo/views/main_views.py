from flask import Blueprint, render_template, session, redirect, g

bp = Blueprint('main', __name__, template_folder='templates', url_prefix='/main')
# 여기서 main 은 url_for 함수에 사용된다.

@bp.route('/')
def index():
    return render_template('main.html')
    # 나중에 회원의 '닉네임'값을 넘겨줘야함. 그래야 출력해줄 수 있음

@bp.route('/logout',methods=['GET'])
def logout():
    session.clear()
    return redirect('/')
