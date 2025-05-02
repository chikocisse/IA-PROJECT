import requests
import json

def get_correction_from_ai(text):
    url = "http://localhost:5000/predict"  # Remplace par l'URL réelle de l'API
    payload = {
        "text": text
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result.get("grade", 0), result.get("feedback", "")
    else:
        return 0, "Erreur de communication avec l'IA"
