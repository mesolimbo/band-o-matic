from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import render

from randomizer.models import Word, Category
from randomizer.picker import generate_band_name
from restapi.serializers import WordSerializer, CategorySerializer


class WordListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_words()

    def get_serializer_class(self):
        return WordSerializer

    @staticmethod
    def get_words():
        return Word.objects.all()


class WordUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_words()

    def get_serializer_class(self):
        return WordSerializer

    @staticmethod
    def get_words():
        return Word.objects.all()


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_categories()

    def get_serializer_class(self):
        return CategorySerializer

    @staticmethod
    def get_categories():
        return Category.objects.all()


class CategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_categories()

    def get_serializer_class(self):
        return CategorySerializer

    @staticmethod
    def get_categories():
        return Category.objects.all()


def random_band_endpoint(request):
    band_name = RandomBandEndpoint.get_band_name()
    return JsonResponse({"band_name": band_name})


class RandomBandEndpoint:
    @staticmethod
    def get_band_name():
        return generate_band_name()


def openapi(request):
    return render(request, "openapi.html", {
        'title': 'OpenAPI Definion of /random/'
    })