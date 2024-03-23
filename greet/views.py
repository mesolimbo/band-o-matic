from django.shortcuts import render
from django.http import HttpResponse
import csv

from randomizer.models import WordCategory
from randomizer.picker import generate_band_name


def generate_band_data():
    band_name = generate_band_name()
    return {
        'band_name': band_name,
        'title': 'Welcome!'
    }


def index(request):
    data = generate_band_data()
    # Use band_name in your context
    return render(request, 'index.html', data)


def privacy(request):
    return render(request, "privacy.html", {
        'title': 'Privacy Policy'
    })


def export_words(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="words.csv"'

    writer = csv.writer(response)
    writer.writerow(['category', 'name'])

    # Fetch all WordCategory objects and sort them by category name and word name
    word_categories = WordCategory.objects.all().order_by('category__name', 'word__name')

    for wc in word_categories:
        writer.writerow([wc.category.name, wc.word.name])

    return response
