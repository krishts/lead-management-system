from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lead
from .forms import LeadForm  # We'll create this next

@login_required
def create_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.agent = request.user
            lead.save()
            return redirect('lead_list')
    else:
        form = LeadForm()
    return render(request, 'leads/create_lead.html', {'form': form})

@login_required
def lead_list(request):
    leads = Lead.objects.filter(agent=request.user)
    return render(request, 'leads/lead_list.html', {'leads': leads})