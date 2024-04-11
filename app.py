from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='site')
 
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template("website.html")


@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)
    output=prediction[0]

    if output==0:
        return render_template('predict.html',pred='You don\'t have heart disease. Woohoo!!')
    else:
        return render_template('predict.html',pred= 'You have heart disease. Please consult the doctor.')


if __name__ == '__main__':
    app.run(debug=True)