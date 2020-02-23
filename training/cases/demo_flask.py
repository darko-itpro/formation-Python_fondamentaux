from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world !"


@app.route('/<demo_var>/')
def var(demo_var):
    return f"url : {demo_var}"


if __name__ == "__main__":
    app.run()