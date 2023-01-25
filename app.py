# command to run flask app: python app.py
# command to run flask app in debug mode: python app.py -d
# flask run --host=http://127.0.0.1:5000 --port=5000 --app=app.py --debug --reload
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'GroceryItems_varinder'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<item %r>' % self.name

with app.app_context():
    db.create_all()

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
    # request has list in query parameters
    if request.args.get('list'):
        groceries = request.args['list'].split(',')
        for grocery in groceries:
            new_item = Todo(name=grocery)
            try:
                db.session.add(new_item)
                db.session.commit()
            except: 
                return "There was an issue adding item to DB"
        return redirect("/foodlist/")
    else:
        groceries = Todo.query.order_by(Todo.date_created).all()
        return render_template("foodlist.html", list_to_buy=groceries)

@app.route("/fooddelete/")
def fooddelete():
    # delete all entries in database
    try:
        num_rows_deleted = db.session.query(Todo).delete()
        db.session.commit()
        return render_template("groceries.html")
    except:
        return "There was a problem deleting items"

if __name__ == "__main__":
    app.run(debug=True)