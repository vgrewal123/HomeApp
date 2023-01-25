# HomeApp

Find the App hosted at : `https://varinderjasmine.herokuapp.com/`

# Hosting app locally

go into root directory: `cd HomeApp`

create virtual env : `python3 -m venv flask-project`

Start virtual environment : `source flask-project/bin/activate`

pip3 install dependencies :`pip3 install -r requirements.txt`

Start Flask app : `python3 app.py` or `flask run --host=http://127.0.0.1:5000 --port=5000 --app=app.py --debug --reload`

go to internet Explorer : `localhost:5000`

# Stop App completely

find the PID : `lsof -i:5000`

kill the process : `kill -9 <PID>`

# hosting app on heroku

install dependencies : `pip3 install gunicorn`

add all dependencies in requirements.txt : `pip freeze > requirements.txt`

Create Proc File with content : `web: gunicorn app:app`

git add commit and push changes to repo.

`heroku login`

`heroku create <unique_app_name>`

`heroku push heroku <branch>(main/master)`
