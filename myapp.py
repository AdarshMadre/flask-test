from flask import Flask 

app = Flask(__name__)

@app.route("/home")
def my_home():
    return "I am at my home"

@app.route("/office")
def my_office():
    return "I am at my office"

@app.route("/gym", methods = ['GET', 'POST'])
def my_gym():
    return "I am at my gym"

if __name__ == "__main__":
    app.run(debug = True)