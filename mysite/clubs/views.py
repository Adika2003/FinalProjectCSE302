from django.shortcuts import render, get_object_or_404
from .models import Club


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})


def club_detail(request, slug):
    club = get_object_or_404(Club, slug=slug)

    # Safely handle related objects (only if relationships exist)
    convener = getattr(club, 'members', None)
    if convener is not None:
        convener = club.members.filter(role_type='convener').first()
        executives = club.members.filter(role_type='executive')
        generals = club.members.filter(role_type='general')
    else:
        convener = executives = generals = None

    events = getattr(club, 'events', None)
    if events is not None:
        events = club.events.all().order_by('start_time')

    posts = getattr(club, 'posts', None)
    if posts is not None:
        posts = club.posts.all().order_by('-published')

    context = {
        'club': club,
        'convener': convener,
        'executives': executives,
        'generals': generals,
        'events': events,
        'posts': posts,
    }

    return render(request, 'clubs/club_detail.html', context)
