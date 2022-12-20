from app import db
from app import login
from datetime import datetime
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

""" defines the classes that SQLAlchemy will map into rows int the proper database tables"""

# association table that demonstrates many-to-many relationship
# a user has many followers, a user follows many users
followers = db.Table('followers',
                     db.Column('follower_id', db.Integer,
                               db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))


class User(UserMixin, db.Model):
    """defines a class and its attributes"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        """recieves a password and generates a unique hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """checks if the password entered is valid, if it is returns True else False"""
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        """generate an avatar for the user"""
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def follow(self, user):
        """handles following a user"""
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        """handles unfollowing"""
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        """"checks if a user is following another user"""
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        """returns posts from the followed users"""
        followed_posts = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)

        # current user's posts
        own = Post.query.filter_by(user_id=self.id)
        # combine user's posts with the posts of the followed users
        return followed_posts.union(own).order_by(Post.timestamp.desc())

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    """ Represents blog posts written by users """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.body}>'


@login.user_loader
def load_user(id):
    """ stores a user's unique identifier to maintain logged in state"""
    return User.query.get(int(id))
