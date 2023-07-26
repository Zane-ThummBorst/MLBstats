from django.urls import path
from . import views


urlpatterns = [
    path('mlb/', views.mlb, name='mlb'),
    path('player/', views.player, name='player'),
    path('search/', views.search, name='search'),
    path('compare/', views.compare, name='compare'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.faq, name='FAQ'),
    path('playerNotFound', views.search, name='playerNotFound')
]