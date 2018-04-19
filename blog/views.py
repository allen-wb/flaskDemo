from flask import Blueprint, render_template, session
from orm import Blog, DBSession

blog = Blueprint('blog', __name__)


@blog.route('/')
def index():
    user_id = session.get('user_id', None)
    if user_id:
        db = DBSession()
        blogs = db.query(Blog).filter(Blog.user_id == user_id).all()
    else:
        # res = ''
        return render_template('login.html')
    return render_template('blog/blog_list.html', result=blogs)
