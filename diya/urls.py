from . import views 
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('wishes/', views.wishes, name='wishes'),  
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),    
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_wish, name='add_wish'),
    path('light-diyas/', views.light_diyas, name='light_diyas'),
    path('get-diyas/', views.get_total_diyas, name='get_diyas')
]
