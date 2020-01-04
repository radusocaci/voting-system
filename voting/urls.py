from django.urls import path
from voting import views

urlpatterns = [
    path("<int:pk>/", views.votedash, name='votedash'),
    path('', views.dashboard, name='dashboard')
]