from flask import Flask
from flask import render_template
import pickle

app = Flask(__name__)
PICKLE_FILE = "/tmp/parsed_articles.pickle"

@app.route("/hn")
def hn():
    with open(PICKLE_FILE, "rb") as f:
        articles = pickle.load(f)
    return render_template("index.html", articles=articles)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

