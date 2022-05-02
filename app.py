from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return '<h1>The about page </h1>'


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
