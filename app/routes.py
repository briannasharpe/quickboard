from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditPostForm, PostForm
from app.models import User, Post
from werkzeug.urls import url_parse
from datetime import datetime
from  sqlalchemy.sql.expression import func

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = User.query.order_by(func.random()).limit(4)
    return render_template('home.html', title='Home Page', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_list/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_list(id):
    form = EditPostForm()
    post = PostForm()
    username = current_user.username
    post = Post.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('user', username=username))
    elif request.method == 'GET':
        form.title.data = post.title
        form.body.data = post.body
    return render_template('edit_list.html', title='Edit List',
                           form=form)

@app.route('/new_list', methods=['GET', 'POST'])
@login_required
def new_list():
    form = PostForm()
    username = current_user.username
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user', username=username)) # redirect to user profile and pass current username
    return render_template('add_list.html', title='New Post', user=user, 
                           form=form)

@app.route('/delete/<int:id>')
@login_required
def delete_post(id):
    username = current_user.username
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('user', username=username))

@app.route('/explore/<username>')
@login_required
def user_explore(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    return render_template('user_explore.html', user=user, posts=posts)