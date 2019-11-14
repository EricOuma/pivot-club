from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('/about', views.AboutView.as_view(), name='about'),
]