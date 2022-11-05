from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)