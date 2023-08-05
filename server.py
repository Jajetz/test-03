#!/usr/bin/env python3

from flask import Flask, request, render_template
import pickle
import yaml
import ruamel.yaml

app = Flask(__name__)

global_variable = ['global_user', '454CA7B2A26E50D8C51572C4D8A023693DDC404F4C563C98DD15818DF83D4F9R']

@app.route('/', methods=['GET'])
def index():

    local_variable = ['local_user', '29C8D2387B3EF2B306855AB19988AE08BB0F558366F5D29AF16732B91D52B62F']

    parameter = request.values.get('parameter')

    parameter1 = eval(parameter)
    parameter2 = pickle.loads(parameter)
    parameter3 = yaml.load(parameter)
    parameter4 = ruamel.yaml.load(parameter)

    res = render_template('index.html', parameter=parameter1)

    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    
