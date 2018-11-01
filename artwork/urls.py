from django.urls import path

from . import views

app_name = 'artwork'
urlpatterns = [
    path('', views.home, name='home'),
    path('sketchbook/', views.sketchbook, name='sketchbook'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
]