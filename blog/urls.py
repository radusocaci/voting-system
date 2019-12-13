from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('<str:category>/', views.blog_category, name='blog_category')
]