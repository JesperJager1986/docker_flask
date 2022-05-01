from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return '<h1>Jeg elsker Anne-Cathrine</h1>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
