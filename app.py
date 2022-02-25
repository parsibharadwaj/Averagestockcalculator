import flask
from flask import render_template, request
from flask_cors import CORS

app = flask.Flask(__name__,)
CORS(app)

@app.route('/',methods=['GET'])
def default():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    #extract data from post request
    X = float(request.form['A'])
    Y = float(request.form['B'])
    Z = float(request.form['C'])
    K = float(request.form['D'])
    v=int(K)
    average=(((X*Y)+(Z*K))/Y+K)
    
    return render_template('predict.html', average=average, sep=v)

if __name__ == '__main__':
    app.run()