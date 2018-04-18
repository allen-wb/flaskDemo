from flask import Blueprint, render_template, request, session, url_for, redirect
from datetime import datetime
from orm import DBSession, User
from utils import get_uuid

user = Blueprint('user', __name__)


@user.route('/to_login')
def to_login():
    return render_template('login.html')


@user.route('/login', methods=['POST'])
def login():
    name = request.form.get('name', default=None)
    password = request.form.get('password', default=None)
    db = DBSession()
    user = db.query(User).filter(User.name == name, User.password == password).first()
    if user:
        db.close()
        session['name'] = name
        session['user_id'] = user.id
        # message = '用户名' + name + '登录成功'
        return redirect(url_for('blog.index'))
    else:
        message = '用户名或密码错误'
        res = {'name': name, 'age': 12, 'sex': '男', 'message': message}

        return render_template('login.html', message=res)


@user.route('/logout', methods=['POST'])
def logout():
    session.pop('name', None)
    session.pop('user_id', None)
    return render_template('index.html')


@user.route('/register', methods=['GET'])
def register():
    return render_template('user/register.html')


@user.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name', default=None)
    password = request.form.get('password', default=None)
    email = request.form.get('email', default=None)
    sex = request.form.get('sex', default=None)
    db = DBSession()
    u = db.query(User).filter(User.name == name).first()
    if u is not None:
        db.close()
        error_message = '用户名' + name + '已存在,请重新输入'
        res = {'code': 100, 'message': error_message, 'data': {'email': email, 'name': name}}
        return render_template('user/register.html', message=res)
    else:
        user = User(id=get_uuid(), name=name, password=password, email=email, sex=sex, create_time=datetime.now())
        db.add(user)
        db.commit()
        db.close()
        res = {'code': 200, 'message': 'success'}
        return render_template('login.html', message=res)


@user.route('/list')
def get_user_list():
    db = DBSession()
    users = db.query(User).all()
    # 使用execute查询,返回的是一个元组集合,在页面可用user[下标获取]
    # ret = session.execute('SELECT user.id AS user_id, user.name AS user_name FROM user')
    return render_template('user/user_list.html', users=users)
