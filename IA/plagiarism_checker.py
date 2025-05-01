from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_similarity(text1: str, text2: str) -> float:
    """
    Calcule une similarité entre deux réponses textuelles.
    Retourne une valeur entre 0 et 1.
    """
    vect = TfidfVectorizer().fit_transform([text1, text2])
    sim = cosine_similarity(vect[0:1], vect[1:2])
    return round(sim[0][0], 3)

# Exemple d'usage :
# score = check_similarity("SELECT * FROM students", "SELECT name FROM students")
# print(score)  # 0.6 par exemple


def analyze_similarity(file_path_1, file_path_2):
    return 0.75  # Valeur fictive de similarité