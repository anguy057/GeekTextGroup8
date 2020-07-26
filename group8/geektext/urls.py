from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genresort/', views.genre, name='genresort'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('ratingsort/', views.rating_sort,name='ratingsort'),
    path('random/', views.random_list,name='random'),
]