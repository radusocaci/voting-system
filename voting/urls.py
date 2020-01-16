from django.urls import path
from voting import views

urlpatterns = [
    path("vote/<int:pk>/", views.votedash, name='votedash'),
    path("vote/<int:candidate_id>/<int:voting_session_id>/", views.vote, name='vote'),
    path('vote/', views.dashboard, name='dashboard'),
    path('results/', views.results_dashboard, name='results_dashboard'),
    path('results/<int:pk>/', views.results_detail, name='results_detail'),
]