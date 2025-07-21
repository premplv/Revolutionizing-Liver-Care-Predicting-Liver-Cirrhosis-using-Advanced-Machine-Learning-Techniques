from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("liver_cirrhosis_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract values from form
        features = [
            float(request.form['Age']),
            float(request.form['Durationofalcoholconsumptionyears']),
            float(request.form['Quantityofalcoholconsumptionquartersday']),
            float(request.form['Hemoglobingdl']),
            float(request.form['PCV']),
            float(request.form['MCVfemtoliterscell']),
            float(request.form['TotalCount']),
            float(request.form['Polymorphs']),
            float(request.form['Lymphocytes']),
            float(request.form['Monocytes']),
            float(request.form['Eosinophils']),
            float(request.form['Basophils']),
            float(request.form['PlateletCountlakhsmm']),
            float(request.form['Directmgdl']),
            float(request.form['Indirectmgdl']),
            float(request.form['TotalProteingdl']),
            float(request.form['Albumingdl']),
            float(request.form['Globulingdl']),
            float(request.form['ALPhosphataseUL']),
            float(request.form['SGOTASTUL']),
            float(request.form['SGPTALTUL'])
        ]

        final_input = np.array(features).reshape(1, -1)
        prediction = model.predict(final_input)

        result = "Patient is not likely to have liver cirrhosis." if prediction[0] == 1 else "Patient is likely to have liver cirrhosis."

        # Instead of rendering the form again, we go to a new page
        return render_template("result.html", prediction=result)

    except Exception as e:
        return f" Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
