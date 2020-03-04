from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world !"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        login_user(username, password)
        return redirect(url_for('index'))
    else:
        display_login_page()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.htmp"), 404


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template("hello.html", name=name)

@app.route('/<demo_var>/')
def var(demo_var):
    return f"url : {demo_var}"


@app.route('/result/')
def result():
    title = request.args['title']
    number = request.args.get('number', default=0, type=int)
    return f"Title : {title} ep : {number * 2}"


if __name__ == "__main__":
    app.run()