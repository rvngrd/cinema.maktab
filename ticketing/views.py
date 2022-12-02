from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Movie, Cinema


def movie_list(request):
    # some decisions
    movies = Movie.objects.all()
    count = len(movies)
    context = {
        'movie_list': movies,
        'count': count
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    # showing movie list
    cinemas = Cinema.objects.all()
    count = len(cinemas)
    context = {
        'cinemas': cinemas,
        'count': count
    }
    return render(request, 'ticketing/cinema_list.html', context)
