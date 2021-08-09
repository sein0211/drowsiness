from pybo import db

class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    # user = db.relationship('User', backref=db.backref('time_table'))
    monClass = db.Column(db.String(200))
    tuesClass = db.Column(db.String(200))
    wedClass = db.Column(db.String(200))
    thursClass = db.Column(db.String(200))
    friClass = db.Column(db.String(200))
    satClass = db.Column(db.String(200))
    sunClass = db.Column(db.String(200))

class DrowsinessData(db.Model):
    __table_name__='DrowsinessData'
    d_data=db.Column(db.Integer,primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    # user = db.relationship('User', backref=db.backref('time_table'))
    d_time=db.Column(db.DateTime,nullable=False)
    d_picture=db.Column(db.String(100),default='Unknown.jpg')
    start_time=db.Column(db.DateTime,nullable=False)
    end_time=db.Column(db.DateTime,nulable=False)

   class User(db.Model):
    user_id = db.Column(db.String(6), primary_key=True, nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    profile_image = db.Column(LargeBinary, nullable = True)
