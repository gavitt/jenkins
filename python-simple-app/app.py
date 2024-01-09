# python
# app.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Привет_, мир!!!'


if __name__ == '__main__':
    app.run(debug=True)
