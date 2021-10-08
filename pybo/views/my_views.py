from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

bp = Blueprint('myPage', __name__, url_prefix='/myPage')


@bp.route('/')
def myPage2():
    return render_template('myPage.html')

@bp.route('/upload')
def upload_file():
    return render_template('myPage.html')

@bp.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return '파일이 성공적으로 업로드되었습니다.'

if __name__ == '__main__':
    bp.run(debug=True)