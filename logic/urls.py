from django.conf.urls import url
from logic import views

urlpatterns = [
    url(r'^api/v1/games/secondloser$', views.secondloser),
]