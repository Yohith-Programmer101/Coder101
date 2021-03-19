from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('<int:id>', projects, name='projects'),
    path('about', about, name='about'),
    path('author', author, name='author'),
    path('d1', login, name='login'),
    path('d1l', loggedin, name='loggedin'),
    path('favicon.ico', favicon, name='favicon.ico'),
]
