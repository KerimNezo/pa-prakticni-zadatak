from ProductArena import app
from ProductArena.forms import LoginForm
from ProductArena.models import User
from ProductArena import db
from flask import render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required

url = "https://www.tech387.com/product-arena/full-stack-developer"


@app.route("/home")
@login_required
def home_page():
    return redirect(url)

@app.route("/login", methods=['GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password = form.password.data
        ):
            login_user(attempted_user)
            return redirect(url_for('home_page'))
        else: 
            flash('Pogresan email ili password')

    #return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("You've been logged out")
    return redirect(url_for('home_page'))
