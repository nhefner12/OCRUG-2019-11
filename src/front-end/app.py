from flask import Flask, render_template, redirect, url_for, request
import os
app = Flask(__name__)

@app.route('/')
def Index():
    return redirect(url_for('Model'))

@app.route('/model')
def Model():
    return render_template('ScoreAssesment.html', active_page="model")


@app.route('/visualization')
def Visualization():
    return render_template('DataVisualization.html', active_page="visualization")

@app.route('/about')
def About():
    return render_template('About.html', active_page="about")

# API calls
@app.route('/generateModel', methods=['POST'])
def GenerateModel():
    name = request.form['field1']
    return name
    # your code
    # return a response


if __name__ == '__main__':
    app.run()
