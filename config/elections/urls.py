from django.urls import path
from .views import list_elections, election_detail, vote

urlpatterns = [
    path('', list_elections, name='list_elections'),
    path('<int:election_id>/', election_detail, name='election_detail'),
    path('vote/<int:candidate_id>/', vote, name='vote'),
]
