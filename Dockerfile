FROM python:slim

# create a my own user instead of root
RUN useradd postit

WORKDIR /home/postit

COPY requirements.txt requirements.txt
# create a virtual environment and install requirements
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt
# install application server
RUN env/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY postit.py config.py boot.sh ./
RUN chmod +x boot.sh
# set an environment variable necessary to use the flask command
ENV FLASK_APP postit.py
# set the owner of all directories and files in WORKDIR as postit user
RUN chown -R postit:postit ./
# set this user as the default
USER postit

EXPOSE 5000
# start the application server when the container is started
ENTRYPOINT ["./boot.sh"]