import requests

def corriger_exercice(reponse_text, api_key):
    """
    Utilise l'API DeepSeek pour corriger une réponse.

    :param reponse_text: str, le texte de la réponse à corriger
    :param api_key: str, votre clé API pour DeepSeek
    :return: dict, la réponse JSON de l'API contenant la correction
    """
    url = "https://api.deepseek.com/correct"  # URL de l'API DeepSeek
    payload = {"text": reponse_text}
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Lève une exception pour les codes HTTP non réussis
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête à l'API DeepSeek: {e}")
        return None
