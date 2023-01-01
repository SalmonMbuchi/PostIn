from app.models import User
from flask_babel import _, lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length


class EditProfileForm(FlaskForm):
    """profile editor"""
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[
                             Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        """accepts the original username as an argument"""
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        """if username is changed make sure its unique"""
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    """follow and unfollow"""
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    """handles creation of posts by users"""
    post = TextAreaField(_l('Say something'), validators=[
                         DataRequired(), Length(min=1, max=1400)])
    submit = SubmitField(_l('Submit'))
