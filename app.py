# command to run flask app: python app.py
# command to run flask app in debug mode: python app.py -d
# flask run --host=http://127.0.0.1:5000 --port=5000 --app=app.py --debug --reload
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/restaurants/")
def restaurants():
    return render_template("restaurants.html")

@app.route("/groceries/")
def groceries():
    return render_template("groceries.html")

@app.route("/list/")
def list():
    return "Hello, World! Here is list of groceries"

@app.route("/list/<int:id>")
def update(id):
    return "Hello, World! the id returned is " + str(id)

@app.route("/foodlist/")
def foodlist():
    groceries = request.args['list'].split(',')
    return render_template("foodlist.html", list_to_buy=groceries)

if __name__ == "__main__":
    app.run(debug=True)