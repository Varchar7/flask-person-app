
from flask import Flask, Response, redirect, render_template, request, url_for
from database import DatabaseService

app = Flask(__name__)

database = DatabaseService()
database.create_table("persons")


@app.route("/", methods=['POST', 'DELETE', 'GET'])
def root():
    if request.method == 'POST':
        response = database.select()
        database.commit()
        return redirect("index.html", response=response)
    elif request.method == 'DELETE':
        print(request.method)
        response = database.delete(
            id=request.values.get("id"),
        )
        database.commit()
        return render_template("index.html", response=response)
    else:
        response = database.select()
        return render_template("index.html", response=response)


@app.route("/<string:id>", methods=['POST', 'GET'])
def individual(id):
    if request.method == 'POST':
        print(request.method)
        response = database.delete(
            id=request.values.get("id"),
        )
        database.commit()
        return render_template("index.html", response=response)
    else:
        # for delete
        if request.values.get("type") == 'delete':
            response = database.delete(
                id=id,
            )
            database.commit()
            return redirect(url_for('root'))
        else:
            response = database.get_by_id(id=id)
            return render_template("look.html", response=response)


@app.route("/look", methods=['POST', 'GET'])
def look():
    if request.method == 'POST':
        if request.values.get("id") == '':
            database.insert(
                name=request.values.get("name"),
                email=request.values.get("email"),
                age=request.values.get("age"),
                number=request.values.get("number")
            )
            return redirect(url_for('look'))
        else:
            database.update(
                id=request.values.get("id"),
                name=request.values.get("name"),
                email=request.values.get("email"),
                age=request.values.get("age"),
                number=request.values.get("number")
            )
            return redirect(url_for('root'))
        database.commit()
    else:
        response = None
        return render_template("look.html", response=response)


app.run(debug=True)
