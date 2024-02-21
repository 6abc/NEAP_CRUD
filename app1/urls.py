from django.urls import path
from app1.views import MovieView
from app1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView, name='HomeView'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += MovieView.get_urls()