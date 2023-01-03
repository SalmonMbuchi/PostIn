from app import create_app, db
from app.models import User, Post

app = create_app()

# app.shell_context_processor decorator registers the function as a shell context function.


@app.shell_context_processor
def make_shell_context():
    """ allows us to import the database and models using the flask shell command """
    # the application is imported by default
    return {'db': db, 'User': User, 'Post': Post}
