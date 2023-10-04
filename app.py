from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, User, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Debug toolbar
toolbar = DebugToolbarExtension(app)

# Connect to the database
connect_db(app)
db.create_all()

# Homepage redirects to list of all users
@app.route('/')
def root():
    return redirect("/users")

# Shows page with info of all users
@app.route('/users')
def users_index():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)

# Form to create a new user
@app.route('/users/new', methods=["GET"])
def users_new_form():
    return render_template('users/new.html')

# Create a new user
@app.route("/users/new", methods=["POST"])
def users_new():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None
    )
    
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

# User profile page
@app.route('/users/<int:user_id>')
def users_show(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

# Edit User form
@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

# Submission form for updating user
@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    user =  User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.commit()

    return redirect("/users")

# Delete existing user
@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")
