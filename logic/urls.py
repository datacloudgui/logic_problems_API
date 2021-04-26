from django.conf.urls import url
from logic import views

urlpatterns = [
    url(r'^api/v1/games/secondloser$', views.secondloser, name= 'pingpong'),
    url(r'^api/v1/passwords/find$', views.password_finder, name='upload_file'),
]