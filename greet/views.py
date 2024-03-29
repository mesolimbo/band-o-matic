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
    response['Content-Disposition'] = 'attachment; filename="export_words.csv"'

    writer = csv.writer(response)
    writer.writerow(['category', 'name'])

    # Fetch all WordCategory objects
    word_categories = WordCategory.objects.all()

    # Sort them by category name and word name, considering lowercase before uppercase
    word_categories = sorted(word_categories, key=lambda w: (w.category.name.lower(), w.word.name.lower()))

    for wc in word_categories:
        writer.writerow([wc.category.name, wc.word.name])

    return response
