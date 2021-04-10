from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('create/', views.create),
    path('<int:w_id>/delete/', views.delete),
]
