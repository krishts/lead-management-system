from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AgentProfile
from .forms import AgentProfileForm  # Create next

@login_required
def update_profile(request):
    profile, created = AgentProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AgentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AgentProfileForm(instance=profile)
    return render(request, 'agents/update_profile.html', {'form': form})

@login_required
def profile(request):
    profile = AgentProfile.objects.get(user=request.user)
    return render(request, 'agents/profile.html', {'profile': profile})