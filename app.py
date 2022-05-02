from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return '<h1>I love Anne-Cathrine</h1>'


@app.route('/about')
def about():
    return '<h1>The about page </h1>'


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
