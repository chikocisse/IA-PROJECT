from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.ai.plagiarism_checker import check_similarity



# Simule les résultats stockés — remplace ça par un modèle plus tard
MOCK_RESULTS = [
    {"studentA": "Alice", "studentB": "Bob", "score": 0.85},
    {"studentA": "Alice", "studentB": "Charlie", "score": 0.32},
    {"studentA": "Bob", "studentB": "Charlie", "score": 0.76},
    {"studentA": "David", "studentB": "Eve", "score": 0.92},
]

@api_view(["GET"])
def get_all_plagiarism_results(request):
    return Response(MOCK_RESULTS)

@api_view(["POST"])
def check_plagiarism(request):
    text1 = request.data.get("text1", "")
    text2 = request.data.get("text2", "")
    if not text1 or not text2:
        return Response({"error": "Deux textes sont requis."}, status=400)
    score = check_similarity(text1, text2)
    return Response({"similarity_score": score})




