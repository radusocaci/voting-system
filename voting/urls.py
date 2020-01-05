from django.urls import path
from voting import views

urlpatterns = [
    path("<int:pk>/", views.votedash, name='votedash'),
    path("<int:candidate_id>/<int:voting_session_id>/", views.vote, name='vote'),
    path('', views.dashboard, name='dashboard'),
    path('<int:voting_session_id/>', views.results_dashboard, name='results_dashboard')
]