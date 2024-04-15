import flask
import pandas as pd
from joblib import dump, load


with open(f'mywork/randomforestmodelasd.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        q1 = flask.request.form['q1']
        q2 = flask.request.form['q2']
        q3 = flask.request.form['q3']
        q4 = flask.request.form['q4']
        q5 = flask.request.form['q5']
        q6 = flask.request.form['q6']
        q7 = flask.request.form['q7']
        q8 = flask.request.form['q8']
        q9 = flask.request.form['q9']
        q10 = flask.request.form['q10']

        input_variables = pd.DataFrame([[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]],
                                       columns=['A1', 'A2', 'A3', 'A4', 'A5','A6', 'A7', 'A8', 'A9', 'A10'],
                                       dtype='int8',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('main.html', original_input={'Rooms': rooms, 'Bathroom': bathroom, 'Landsize': landsize, 'Lattitude': lattitude, 'Longtitude': longtitude, 'Distance': distance, 'Car': car, 'Landsize': landsize, 'BuildingArea': buildingarea, 'YearBuilt': yearbuilt},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
