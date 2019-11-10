from flask import Flask, render_template, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def Index():
    return redirect(url_for('Model'))

@app.route('/model')
def Model():
    return render_template('ScoreAssesment.html')


@app.route('/visualization')
def Visualization():
    return render_template('DataVisualization.html')

@app.route('/about')
def About():
    return render_template('About.html')


if __name__ == '__main__':
    app.run()
