from flask import Flask, request, render_template
import utils
from orm import User, DBSession

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def sign_in():
    return render_template('form.html')


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
