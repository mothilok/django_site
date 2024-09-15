from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('create_poster', views.create_poster, name='create_poster')
]