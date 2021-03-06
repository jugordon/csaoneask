"""
Definition of urls for solicitudesCSA.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from csa import forms, views


urlpatterns = [
    path('', views.csarequest, name='csarequest'),
    path('requestReceived/', views.requestReceived, name='requestReceived'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('csarequest/', views.csarequest, name='csarequest'),
    path('about/', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='csa/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('ajax_load_techs/', views.load_techs, name='ajax_load_techs'),
    path('admin/', admin.site.urls),
]
