from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Event
from .forms import EventForm
from django.utils import timezone

def event_list(request):
    events = Event.objects.order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

# JSON feed for FullCalendar or other JS calendar
def events_json(request):
    events = Event.objects.filter(end_time__gte=timezone.now()).order_by('start_time')
    data = []
    for e in events:
        data.append({
            'title': e.title,
            'start': e.start_time.isoformat(),
            'end': e.end_time.isoformat() if e.end_time else None,
            'url': e.get_absolute_url(),
        })
    return JsonResponse(data, safe=False)
