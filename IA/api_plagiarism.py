from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import PlagiarismResultSerializer
from .models import PlagiarismResult


# Pagination
class PlagiarismResultPagination(PageNumberPagination):
    page_size = 10  # Vous pouvez ajuster la taille de la page selon vos besoins

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # S'assurer que l'utilisateur est authentifié
def get_all_plagiarism_results(request):
    try:
        results = PlagiarismResult.objects.all().order_by('-created_at')  # Trier par date décroissante
        
        if not results:
            return Response({"message": "Aucun résultat de plagiat trouvé."}, status=404)
        
        paginator = PlagiarismResultPagination()  # Utilisation de la pagination
        paginated_results = paginator.paginate_queryset(results, request)
        
        # Sérialisation des résultats paginés
        serializer = PlagiarismResultSerializer(paginated_results, many=True)
        
        # Retourner la réponse paginée
        return paginator.get_paginated_response(serializer.data)
    
    except Exception as e:
        # Retourner une réponse d'erreur en cas de problème
        return Response({"error": f"Erreur lors de la récupération des résultats : {str(e)}"}, status=500)
