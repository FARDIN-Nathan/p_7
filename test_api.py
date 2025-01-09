import pytest
import requests
client_test = 400958
def test_id_valable():
  response = requests.get(f'https://6equal.pythonanywhere.com/predict/{client_test}')
  assert response.status_code == 200
  assert isinstance(response.json(), dict)
  
client_test_bad_id = 40095
def test_bad_id():
  response = requests.get(f'https://6equal.pythonanywhere.com/predict/{client_test_bad_id}')
  assert response.status_code == 404
  # Vérification de la réponse
  json_response = response.json()
  expected_error = {"error": f"ID : {client_test_bad_id} not found"}
  assert json_response == expected_error, f"Expected {expected_error}, but got {json_response}"
  
def test_good_response_exact_content():
  response = requests.get(f'https://6equal.pythonanywhere.com/predict/{client_test}')
  assert response.status_code == 200
  # Vérification de la réponse
  json_response = response.json()
  expected_response = {"client_id":400958,"details":"grant_loan","prediction":0,"probability":{"will_not_pay":0.24878239307664046,"will_pay":0.7512176069233596}}
  assert json_response == expected_response, f"En attente de {expected_response},mais obtenue {json_response}"
  

def test_response_keys():
    response = requests.get(f'https://6equal.pythonanywhere.com/predict/{client_test}')
    assert response.status_code == 200, f"Statut attendu 200, mais obtention de {response.status_code}"
    # Vérification de la réponse
    json_response = response.json()
    # Clés attendues
    expected_keys = ["client_id", "details", "prediction", "probability"]
    probability_keys = ["will_not_pay", "will_pay"]

    assert all(key in json_response for key in expected_keys), f"Clés manquantes. Clés attendues: {expected_keys}, obtenues : {list(json_response.keys())}"
    assert all(key in json_response["probability"] for key in probability_keys), f"Manque de clés 'probability'. Clés attendues: {probability_keys}, obtenues: {list(json_response['probability'].keys())}"