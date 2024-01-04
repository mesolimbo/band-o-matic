from django.shortcuts import render

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
