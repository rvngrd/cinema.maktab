from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from ticketing.models import Movie, Cinema, ShowTime, Ticket


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
    showtimes = ShowTime.objects.all().order_by('price')
    context = {
        'showtimes': showtimes
    }
    return render(request, 'ticketing/showtime_list.html', context)


@login_required
def showtime_details(request, showtime_id):
    showtime = ShowTime.objects.get(pk=showtime_id)
    context = {
        'showtime': showtime
    }
    # Buy tickets
    if request.method == 'POST':
        try:
            seat_count = int(request.POST['seat_count'])
            assert showtime.status == showtime.SALE_OPEN, 'خرید بلیت برای این سانس امکان پذیر نیست'
            assert showtime.free_seats >= seat_count, 'به اندازه مقدار انتخاب شده صندلی خالی وجود ندارد'
            total_price = showtime.price * seat_count
            assert request.user.profile.spend(total_price), 'موجودی کافی نیست'
            Ticket.objects.create(showtime=showtime, customer=request.user.profile, seat_count=seat_count)
        except Exception as e:
            context['error'] = str(e)
    #
    return render(request, 'ticketing/showtime_details.html', context)


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(customer=request.user.profile).order_by('-order_time')
    context = {
        'tickets': tickets
    }
    return render(request, 'ticketing/ticket_list.html', context)


@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'ticketing/ticket_details.html', context)
