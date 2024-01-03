from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
import rest_framework.generics

from randomizer.models import Word, Category
from randomizer.picker import generate_band_name
from restapi.serializers import WordSerializer, CategorySerializer


# This API view works with Word model
class WordListCreateAPIView(rest_framework.generics.ListCreateAPIView):
    """This endpoint allows for listing all words in the database (GET), or creating one (POST)"""
    permission_classes = [IsAuthenticated]
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    """This endpoint allows for retrieving single word, updating, or deleting a word."""
    permission_classes = [IsAuthenticated]
    queryset = Word.objects.all()
    serializer_class = WordSerializer


# These API views work with Category model
class CategoryListCreateAPIView(rest_framework.generics.ListCreateAPIView):
    """This endpoint allows for listing (GET) all categories in the database, or creating one (POST)"""
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    """This endpoint allows for deleting (DELETE) a category from the database by passing the ID to delete"""
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def random_band_endpoint(request):
    band_name = generate_band_name()

    # Return the band name as JSON
    return JsonResponse({"band_name": band_name})
