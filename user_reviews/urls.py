from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='user_reviews'),
]
