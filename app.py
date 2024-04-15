from __future__ import with_statement
import flask

import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from joblib import dump, load


with open('./randomforestmodelasd.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))
    if flask.request.method == 'POST':
      #  a1 = int(flask.request.form['a1'])
        a1 =  int(flask.request.form['a1'])
        a2 = int(flask.request.form['a2'])
        a3 = int(flask.request.form['a3'])
        a4 = int(flask.request.form['a4'])
        a5 = int(flask.request.form['a5'])
        a6 = int(flask.request.form['a6'])
        a7 = int(flask.request.form['a7'])
        a8 = int(flask.request.form['a8'])
        a9 = int(flask.request.form['a9'])
        a10 = int(flask.request.form['a10'])
        age = int(flask.request.form['age'])
        jaundice = int(flask.request.form['jaundice'])
        sex = int(flask.request.form['sex'])
        familyasd = int(flask.request.form['familyasd'])
        print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

          
        input_variables = pd.DataFrame([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,age,sex,jaundice,familyasd]],
                                       columns=['A1', 'A2', 'A3', 'A4', 'A5','A6', 'A7', 'A8', 'A9', 'A10','Age_Mons','Sex','Jaundice','Family_mem_with_ASD'],
                                       dtype='int',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)
        if predictions == 1:
            result1 = f'Potential to ASD trait. Please Consult Doctor'
        else:
            result1 = 'NO Autism is predicted.'
        return flask.render_template('result.html', original_input={'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8, 'A9': a9, 'A10': a10, 'Age_Mons': age, 'Sex': sex, 'Jaundice': jaundice, 'Family_mem_with_ASD': familyasd},
                                     result=result1)


if __name__ == '__main__':
    app.run(debug=True)
