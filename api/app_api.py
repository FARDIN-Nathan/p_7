import os
import pickle
import pandas as pd
from flask import Flask, jsonify

os.environ["LOKY_MAX_CPU_COUNT"] = "1"

with open("/home/6equal/api/model_lgbm.pkl", 'rb') as file:
    model = pickle.load(file)

data_api=pd.read_csv("/home/6equal/api/api_test_pe.csv")
# Initialiser Flask
app = Flask(__name__)

#API pour prédire le remboursement ou non d'un prêt
@app.route('/predict/<int:client_id>', methods=['GET'])
def predict(client_id):

    # Vérifier si l'ID du client existe dans les données
    client_data = data_api[data_api['SK_ID_CURR'] == client_id]
    if client_data.empty:
        return jsonify({"error": f"ID : {client_id} not found"}), 404
    features = client_data
    # Vérification des données
    if features.empty:
        return jsonify({"error": f"No valid features available for client : {client_id}"}), 400

    # Prédiction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].tolist()
    if int(prediction)==0:
        details="grant_loan"
    elif int(prediction==1):
        details="do_not_grant_loan"

    # Construction de la réponse
    response = {
        "client_id": client_id,
        "prediction": int(prediction),
        "details": details,
        "probability": {
            "will_not_pay": probability[1],
            "will_pay": probability[0]
        }
    }

    return jsonify(response)