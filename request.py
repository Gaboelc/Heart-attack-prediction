import requests

# URL de la API
url = "http://127.0.0.1:5000/predict"

# Datos de prueba del paciente
patient_data = {
    "age": 62,
    "sex": 1,
    "cp": 1,
    "trestbps": 120,
    "chol": 200,
    "fbs": 0,
    "restecg": 1,
    "thalach": 140,
    "exang": 0,
    "oldpeak": 1.4,
    "slope": 2,
    "ca": 1,
    "thal": 3
}

# Envía una solicitud POST a la API con los datos del paciente
response = requests.post(url, json=patient_data)

# Imprime la respuesta de la API
print(response.json())
