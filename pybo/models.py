from pybo import db

class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('time_table'))
    monClass = db.Column(db.String(200))
    tuesClass = db.Column(db.String(200))
    wedClass = db.Column(db.String(200))
    thursClass = db.Column(db.String(200))
    friClass = db.Column(db.String(200))
    satClass = db.Column(db.String(200))
    sunClass = db.Column(db.String(200))

class DrowsinessData(db.Model):
    __table_name__='DrowsinessData'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('d_data_set'))
    d_time = db.Column(db.DateTime,nullable=False)
    d_picture = db.Column(db.String(100),default='Unknown.jpg')
    start_time = db.Column(db.DateTime,nullable=False)
    end_time = db.Column(db.DateTime,nullable=False)
    
class User(db.Model):
    __table_name__='User'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(7), nullable=False, unique=True)
    nickname = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(20), nullable=False)
