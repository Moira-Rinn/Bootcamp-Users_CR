from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.user import User


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create/user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
    }
    User.save(data)
    return redirect('/users')


@app.route('/users')
def user():
    query = "SELECT * FROM users;"
    users = User.get_all(query)
    return render_template("results.html", all_users=users)


@app.route('/show/<int:user_id>')
def detail_page(user_id):
    query = "SELECT * FROM users WHERE users.id = %(id)s;"
    data = {
        'id': user_id
    }

    results = User.get_all(query, data)

    return render_template("details_page.html", user=results[0])
