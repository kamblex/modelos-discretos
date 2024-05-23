from flask import Flask, render_template, request
import numpy as np
from scipy.stats import poisson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    lmbda = float(request.form['lambda'])
    k = int(request.form['k'])

    # Calcular la probabilidad de k eventos
    probability = poisson.pmf(k, lmbda)

    return render_template('result.html', probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
