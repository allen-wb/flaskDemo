from flask import Flask, request, render_template
import utils
from orm import User, DBSession

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/example')
def example():
    message = "Hello Flask!"
    return render_template('example.html', message=message)


@app.route('/more')
def more():
    return render_template('more.html')


@app.route('/router')
def router():
    return render_template('router.html')


@app.route('/sfc')
def sfc():
    return render_template('sfc.html')


@app.route('/typescript')
def typescript():
    return render_template('typescript.html')


@app.route('/vuex')
def vuex():
    return render_template('vuex.html')


@app.route('/v0.10.3')
def v0_10_3():
    return render_template('vue.js_v0.10.3.html')


@app.route('/vue_test', methods=['GET'])
def vue_test():
    return render_template('vueTest.html')


@app.route('/signin', methods=['GET'])
def sign_in():
    return render_template('form.html', message='wb')


@app.route('/signin', methods=['POST'])
def save_user():
    name = request.form['name']
    password = request.form['password']
    user = User(id=utils.get_uuid(), name=name)
    session = DBSession()
    session.add(user)
    session.commit()
    session.close()
    return render_template('signin-ok.html', name=name)


if __name__ == '__main__':
    app.run()
