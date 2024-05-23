from flask import Flask , render_template , request
import numpy as np
from scipy . stats import binom
app = Flask ( __name__ )

@app . route (’/’)
def index () :
return render_template (’index . html ’)
@app . route (’/ calculate ’, methods =[ ’POST ’])
def calculate () :
n = int( request . form [’n’])
p = float ( request . form [’p’])
x = int( request . form [’x’])

# Calcular la probabilidad binomial
probability = binom . pmf (x , n , p )

return render_template (’result . html ’, probability = probability )

if __name__ == ’__main__ ’:
app . run ( debug = True )
