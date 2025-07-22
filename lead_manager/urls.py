from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings  # Add this import
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth import views as auth_views
from leads.views import create_lead, lead_list
from agents.views import update_profile, profile

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-lead/', create_lead, name='create_lead'),
    path('leads/', lead_list, name='lead_list'),
    path('profile/', profile, name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)