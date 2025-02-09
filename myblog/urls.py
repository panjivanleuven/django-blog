from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('kategori/<slug:slug>/', views.kategori_detail, name='kategori_detail'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
]