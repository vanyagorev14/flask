import random
from flask import Flask, jsonify
import csv
from faker import Faker
import requests, json
import numpy as np

app = Flask(__name__)
fake = Faker()


@app.route("/requirements/")
def open_func():
    my_file = open('requirements.txt', "r")
    my_string = my_file.read()
    return f'<p>{my_string}</p>'


@app.route("/generate-users/")
@app.route("/generate-users/<int:count>")
def function(count=100):
    guys, result = '', ''
    for i in range(count):
        guys = f'<p>{Faker().email()}</p>'
        result += guys
    return result


@app.route('/space')
def austronaut():
    re = requests.get('http://api.open-notify.org/astros.json')
    res = f'<p>Astronauts we have:  {len(re.json()["people"])}</p>'
    for el in re.json()['people']:
        res += f'<p>{el["name"]}</p>'
    return res



@app.route("/mean/")
def funk():
    with open('hw.csv', newline='') as f:
        reader = list(csv.reader(f))
        reader.pop(0)
        for i in range(len(reader)):
            for g, score in enumerate(reader[i]):
                reader[i][g] = float(score)

        array = np.array(reader)
        consult = f'<p>Average weight: {array.mean(axis=0)[1]}</p> /' \
              f'<p>Average height: {array.mean(axis=0)[2]}</p>'
    return consult

if __name__ == "__main__":
    app.run(debug=True)
