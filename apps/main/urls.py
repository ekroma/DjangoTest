from django.urls import path
from .views import RoomList, RoomRetrieve

urlpatterns = [
    path('lists/', RoomList.as_view()),
    path('<str:room_id>/', RoomRetrieve.as_view())
]