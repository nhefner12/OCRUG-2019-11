from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def Model():
    return render_template('ScoreAssesment.html')


@app.route('/Visualization')
def Visualization():
    return render_template('DataVisualization.html')


if __name__ == '__main__':
    app.run()
