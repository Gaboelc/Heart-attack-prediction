from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load('./models/svm_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtiene los datos del paciente desde la solicitud POST
        input_data = request.get_json()

        # Convierte los datos del paciente en un DataFrame
        patient_data = pd.DataFrame(input_data, index=[0])

        # Aplica la transformación scaler a los datos del paciente
        patient_data = scaler.transform(patient_data)

        # Realiza la predicción utilizando el modelo SVM
        prediction = model.predict(patient_data)

        # Devuelve el resultado como una respuesta JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) #debug=TRUE
