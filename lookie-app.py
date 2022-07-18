from flask import Flask, redirect, render_template, request, url_for
from database import DatabaseService

app = Flask(__name__)

database = DatabaseService()
database.create_table("persons")


@app.route("/")
def root():
    response = database.select()
    database.commit()
    return render_template("index.html", response=response)


@app.route("/look", methods=['POST', 'GET'])
def look():
    if request.method == 'POST':
        database.insert(
            name=request.values.get("name"),
            email=request.values.get("email"),
            age=request.values.get("age"),
            number=request.values.get("number")
        )
        database.commit()
        return redirect(url_for('look'))
    else:
        return render_template("look.html")


app.run(debug=True)
