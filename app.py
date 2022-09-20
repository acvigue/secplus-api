import re
from flask import Flask, request
from secplus import encode_v2_manchester

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def hello():
    print(request.form)
    return str(encode_v2_manchester(request.form['rolling_code'], request.form['fixed_code']))


if __name__ == "__main__":
    app.run(debug=True)