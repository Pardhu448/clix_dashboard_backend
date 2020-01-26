from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm
from app.models.user.schema import User
from app.models.school.schema import Metric1, Metric2

#from app.models import user, syncstatus

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', title='CLIx Dashboard')

'''
@app.route('/syncstatus')
@login_required
def syncstatus():
    page = request.args.get('page', 1, type=int)
    syncstatus_live = syncstatus.Service.get_sync_status().paginate(
    page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=syncstatus_live.next_num) \
        if syncstatus_live.has_next else None
    prev_url = url_for('index', page=syncstatus_live.prev_num) \
        if syncstatus_live.has_prev else None

    return render_template('index.html', title='SyncStatus', syncedschools=syncstatus_live.items,
                           next_url=next_url, prev_url=prev_url)
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #userlogged = user.Service.find_user(username=form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None :
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
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
    page = request.args.get('page', 1, type=int)
    schoolstatus = SyncStatus.query.order_by(SyncStatus.lastupdated.desc()).paginate(
    page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=schoolstatus.next_num) \
        if schoolstatus.has_next else None
    prev_url = url_for('index', page=schoolstatus.prev_num) \
        if schoolstatus.has_prev else None

    return render_template('index.html', title='SyncStatus', username=user, schools=schoolstatus.items,
                           next_url=next_url, prev_url=prev_url)
