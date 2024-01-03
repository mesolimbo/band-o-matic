from django.shortcuts import render

from randomizer.picker import generate_band_name


def index(request):
    band_name = generate_band_name()

    # Use band_name in your context
    return render(request, 'index.html', {
        'band_name': band_name,
        'title': 'Welcome!'
    })


def privacy(request):
    return render(request, "privacy.html", {
        'title': 'Privacy Policy'
    })
