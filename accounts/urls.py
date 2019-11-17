from django.urls import path
from accounts import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('sigiin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]