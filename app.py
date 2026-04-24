from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    data = []

    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                data.append(row)
    except:
        pass

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)