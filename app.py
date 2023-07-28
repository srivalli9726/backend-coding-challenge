import logging

from flask import Flask

from endpoints.suggestions import suggestions_bp

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s in %(module)s : %(message)s')

app.register_blueprint(suggestions_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
