from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/fake_profile_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['profile_pic']),
        float(request.form['nums_username']),
        float(request.form['fullname_words']),
        float(request.form['nums_fullname']),
        float(request.form['name_username']),
        float(request.form['description_length']),
        float(request.form['external_url']),
        float(request.form['private']),
        float(request.form['posts']),
        float(request.form['followers']),
        float(request.form['follows'])
    ]

    final_features = np.array(features).reshape(1, -1)

    prediction = model.predict(final_features)[0]

    probability = model.predict_proba(final_features)[0]

    confidence = round(max(probability) * 100, 2)

    result = "Fake Profile" if prediction == 1 else "Real Profile"

    return render_template(
        'result.html',
        prediction=result,
        confidence=confidence
    )

if __name__ == '__main__':
    app.run(debug=True)