from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Member
from Clubs.models import Club
from .forms import MemberForm


# 🔹 Show all members of a specific club
def member_list(request, club_slug):
    club = get_object_or_404(Club, slug=club_slug)

    # Ensure 'members' related_name exists on Member model
    members_qs = getattr(club, 'members', None)
    if members_qs is not None:
        convener = club.members.filter(role_type='convener').first()
        executives = club.members.filter(role_type='executive')
        generals = club.members.filter(role_type='general')
    else:
        convener = executives = generals = None

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
            updated_member = form.save(commit=False)
            updated_member.save()

            # Redirect to member list of that club if exists
            if updated_member.club:
                return redirect('members:list', club_slug=updated_member.club.slug)
            else:
                return redirect('clubs:list')
    else:
        form = MemberForm(instance=member)

    context = {
        'form': form,
        'member': member,
    }
    return render(request, 'members/member_form.html', context)
