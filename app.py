from flask import Flask, render_template
from user.views import user
from blog.views import blog

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(blog, url_prefix='/blog')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)  # 调试模式
