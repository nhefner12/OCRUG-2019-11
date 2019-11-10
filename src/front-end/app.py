from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import pickle
import os
app = Flask(__name__)

filename = open('ocrug_finalized_model.sav','rb')
model = pickle.load(filename)

@app.route('/')
def Index():
    return redirect(url_for('Model'))

@app.route('/model')
def Model():
    return render_template('ScoreAssesment.html', active_page="model")


@app.route('/visualization')
def Visualization():
    return render_template('DataVisualization.html', active_page="visualization")

@app.route('/team')
def About():
    return render_template('Team.html', active_page="team")

# API calls
@app.route('/generateModel', methods=['POST'])
def GenerateModel():
    values = request.form.to_dict()
<<<<<<< HEAD
    df = pd.DataFrame(values, index=[0])
    df_onehot=pd.get_dummies(df,columns=['day_bin','pdays_bin','job','marital','education','default','housing','loan','contact','poutcome'])
    prediction = model.predict_proba(df_onehot.values)
=======
    print(values)
    return 'hi'
>>>>>>> 92753c57016f896b45888e81ce09803a07dd7816

    return render_template("ScoreAssessment.html", prediction = prediction)

if __name__ == '__main__':
    app.run()
