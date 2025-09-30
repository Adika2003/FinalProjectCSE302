from django.shortcuts import render, get_object_or_404
from .models import Club


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})


def club_detail(request, slug):
    club = get_object_or_404(Club, slug=slug)


    members = club.members.all()


    events = club.events.all().order_by('start_time')


    posts = club.posts.all().order_by('-published')

    return render(request, 'clubs/club_detail.html', {
        'club': club,
        'members': members,
        'events': events,
        'posts': posts,
    })
