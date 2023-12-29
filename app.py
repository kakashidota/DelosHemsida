from flask import Flask, render_template




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/potatis")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)