import sqlite3

from flask import abort
from flask import Flask
from flask import g
from flask import Markup
from flask import render_template


app = Flask(__name__)
app.config.from_object('config')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_slugs():
    cur = get_db().cursor()
    cur.execute('select slug,title from posts')
    titles = cur.fetchall()
    return titles


def get_post_by_slug(slug):
    cur = get_db().cursor()
    cur.execute('select * from posts where slug = ?', (slug,))
    return cur.fetchone()


def post_to_dict(post_row):
    d = {}
    d['title'] = post_row[1]
    d['date'] = post_row[2]
    d['content'] = Markup(post_row[3])
    return d


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    slugs = get_slugs()
    return render_template('index.html', slugs=slugs)


@app.route('/<slug>')
def post(slug):
    post = get_post_by_slug(slug)
    if not post:
        abort(404)
    return render_template('post.html', post=post_to_dict(post))


if __name__ == '__main__':
    app.run()
