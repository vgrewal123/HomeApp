from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/restaurants/")
def restaurants():
    return "Welcome to restaurants page!!"

@app.route("/groceries/")
def groceries():
    return "Welcome to Groceries page!!"

@app.route("/dish/<int:id>")
def update(id):
    return "Hello, World! the id returned is " + str(id)

if __name__ == "__main__":
    app.run(debug=True)