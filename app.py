import random

import numpy as np
import requests
from flask import Flask, jsonify
from faker import Faker
import csv

app = Flask(__name__)


@app.route("/requirements/")
def hello_name():
    with open('requirements.txt', 'r') as requirements:
        # return f'<p>{requirements.read()}</p>'
        res = ''
        for el in requirements.read().split():
            res += f'<p>{el}</p>'
        return res


@app.route("/generate-users/")
@app.route("/generate-users/<int:count>")
def gen_users_count(count=100):
    user, res = '', ''
    for i in range(count):
        fake = Faker().name()
        name = fake.split()[0] if fake.split()[0][-1] != '.' else fake.split()[1]
        user = f'<p>{name} {Faker().email()}'
        res += user
    return res


@app.route("/mean/")
def avg():
    with open('hw.csv', newline='') as File:
        reader = list(csv.reader(File))
        reader.pop(0)
        for i in range(len(reader)):
            for j, item in enumerate(reader[i]):
                reader[i][j] = float(item)

        array = np.array(reader)
        res = f'<p>Average weight: {array.mean(axis=0)[1]}</p> <p>Average height: {array.mean(axis=0)[2]}</p>'
    return res


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')

    res = f'<p>Count of astronauts: {len(r.json()["people"])}</p>'
    for el in r.json()['people']:
        res += f'<p>{el["name"]}</p>'

    return res