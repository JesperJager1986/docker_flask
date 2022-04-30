from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'test'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    homepage()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
