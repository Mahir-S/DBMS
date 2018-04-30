from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'book'
urlpatterns = [
    path('home/', views.home,),
    path('match/',views.match,),
    path('signup/',views.signup,),
    path('login/',auth_view.login,name='login', kwargs={'template_name': 'book/login.html'}),
    path('logout/', auth_view.logout, name='logout', kwargs={'next_page': 'http://127.0.0.1:8000/home/'}),
    path('book/<int:id>/',views.book,),
    path('profile/',views.profile),
    path('profile/<int:id>/<str:s>/<int:tno>/',views.delete_ticket),
    path('modify/',views.modify),
]
