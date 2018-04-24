from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('home/', views.home,),
    path('match/',views.match)
    
]
