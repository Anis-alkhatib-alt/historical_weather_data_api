from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def get_temp(station, date):


if __name__ == "__main__":
    app.run(debug=True)
