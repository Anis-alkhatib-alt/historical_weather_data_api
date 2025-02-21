from datetime import datetime

from flask import Flask, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def get_temp(station, date):
    df = pd.read_csv(
        "./data/TG_STAID" + station.zfill(6) + ".txt",
        skiprows=20,
        parse_dates=['    DATE'],
    )
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    df["TG"] = df["TG0"] / 10
    temp = df.loc[df['    DATE'] == date]["TG"].squeeze()
    date_object = datetime.strptime(date, "%Y%m%d")
    displate_date = datetime.strftime(date_object, "%d-%m-%Y")
    result = {"Station": station, "Date": displate_date, "Temprature": temp}
    return result


if __name__ == "__main__":
    app.run(debug=True)
