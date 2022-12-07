from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from ticketing.models import Movie, Cinema, ShowTime


def movie_list(request):
    # some decisions
    movies = Movie.objects.all()
    count = len(movies)
    context = {
        'movies': movies,
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


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)


def cinema_details(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)


def showtime_list(request):
    request.user
    showtimes = ShowTime.objects.all().order_by('price')
    context = {
        'showtimes': showtimes
    }
    return render(request, 'ticketing/showtime_list.html', context)

