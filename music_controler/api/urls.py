from django.urls import path, include
from .views import RoomView


urlpatterns = [
    # Define your API endpoints here
    path('rooms/', RoomView.as_view(), name='room-list-create'),
]