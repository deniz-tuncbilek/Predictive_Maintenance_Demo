import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    features_array = [np.array(features)]
    prediction = model.predict(features_array)
    output = int(prediction[0])
    return render_template('index.html',
                           prediction_text='Remaining useful life is: {} cycles'.format(output))


@app.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(list(data.values())))
    output = 27#prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
