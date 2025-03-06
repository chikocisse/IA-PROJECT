from ai.correction import corriger_exercice

# Cle API DeepSeek
API_KEY = "VOTRE_CLE_API"

# Exemple de réponse à corriger
reponse_text = "Le chat est sur le tapis."

# Correction de la réponse
correction = corriger_exercice(reponse_text, API_KEY)

if correction:
    print("Correction réussie:", correction)
else:
    print("La correction a échoué.")