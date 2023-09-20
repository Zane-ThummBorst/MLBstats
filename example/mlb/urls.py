from django.urls import path
from . import views


urlpatterns = [
    path('mlb/', views.mlb, name='mlb'),
    path('player/', views.player, name='player'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.faq, name='FAQ'),
    path('playerNotFound', views.search, name='playerNotFound'),
    path('roster_search', views.roster_search, name="roster_search"),
    path('roster_info/', views.roster_info, name="roster_info")
]