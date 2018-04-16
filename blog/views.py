from flask import Blueprint, render_template, request

blog = Blueprint('blog', __name__)


@blog.route('/')
def index():
    return render_template('blog/index.html', message='test')
