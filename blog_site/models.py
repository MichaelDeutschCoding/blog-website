from blog_site import db
from sqlalchemy import func


class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    f_name = db.Column(db.String(64), nullable=False)
    l_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    registration_date = db.Column(db.DateTime(timezone=False), server_default=func.now())
    blogs = db.relationship('blog', backref='user', lazy=True)


tags = db.Table('tags',
                db.Column('blog_id', db.Integer,
                          db.ForeignKey('blog.blog_id'), primary_key=True),
                db.Column('tag_id', db.Integer,
                          db.ForeignKey('tag.tag_id'), primary_key=True)
                )


class Blog(db.Model):
    blog_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.relationship('tag', secondary=tags, lazy='subquery',
                           backref=db.backref('tags', lazy=True))
    date = db.Column(db.DateTime(timezone=False), server_default=func.now())


class Tag(db.Model):
    tag_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)


