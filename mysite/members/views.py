from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Member
from clubs.models import Club
from .forms import MemberForm


# 🔹 Show all members of a specific club
def member_list(request, club_slug):
    club = get_object_or_404(Club, slug=club_slug)

    members = Member.objects.filter(club=club)
    convener = members.filter(role_type='convener').first()
    executives = members.filter(role_type='executive')
    generals = members.filter(role_type='general')

    context = {
        'club': club,
        'convener': convener,
        'executives': executives,
        'generals': generals,
    }
    return render(request, 'members/member_list.html', context)


# 🔹 Update a member profile
@login_required(login_url='/login/')
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            updated_member = form.save()
            if updated_member.club:
                return redirect('member_list', club_slug=updated_member.club.slug)
            return redirect('club_list')
    else:
        form = MemberForm(instance=member)

    context = {
        'form': form,
        'member': member,
    }
    return render(request, 'members/member_form.html', context)
