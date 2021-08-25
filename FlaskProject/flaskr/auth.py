import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


def get_user_and_pass(form):
    return {
        'username':  form.get('username', None),
        'password': form.get('password', None)
    }


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        user_and_pass = get_user_and_pass(request.form)
        connection = get_db()
        error = None

        if not user_and_pass.get('username'):
            error = 'Username is required.'
        elif not user_and_pass.get('password'):
            error = 'Password is required.'

        if error is None:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO user (username, password) VALUES ('%s', '%s')" % (
                    user_and_pass.get('username'),
                    generate_password_hash(user_and_pass.get('password'))
                )
                cursor.execute(query)
                connection.commit()
            except db.IntegrityError:
                error = f"User {user_and_pass.get('username')} is already registered."
            except Exception as Error:
                raise ValueError(Error)
            else:
                return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user_and_pass = get_user_and_pass(request.form)
        connection = get_db()
        error = None
        check_password = False
        cursor = connection.cursor()
        user = cursor.execute(
            'SELECT * FROM user WHERE username = ?', (user_and_pass.get('username'),)
        ).fetchone()
        if user:
            check_password = check_password_hash(
                user['password'],
                user_and_pass.get('password')
            )

        if user is None:
            error = 'Incorrect username'
        elif not check_password:
            error = 'Incorrect password'

        if check_password:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
