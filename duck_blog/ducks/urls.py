from django.urls import path
from ducks.views import (
    duckListView,
    duckDetailView,
)

urlpatterns = [
    path('duck-list', duckListView.as_view(), name='duck_list'),
    path('duck-detail/<int:pk>', duckDetailView.as_view(), name='duck_detail'),
]