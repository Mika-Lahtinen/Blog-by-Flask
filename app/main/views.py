from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def say_Hello():
    form = NameForm()
    if form.validate_on_submit():

        user = User.query.filter_by(table_username=form.name.data).first()
        if user is None:
            user = User(table_username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASK_ADMIN']:
                send_email(app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True

        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Are you changing your name?')
        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('.say_hello'))

    return render_template('say_Hello.html', current_time=datetime.utcnow(),
                           custom_name=session.get('name'), initialed_form=form,
                           known=session.get('known', False))


@main.route('/user/<name>')
def say_Hello_to_User(name):
    return render_template('say_Hello_to_User.html', user_name=name)
