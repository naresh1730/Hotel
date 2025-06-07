from django.urls import path
from .views import RoomListView, BookingList, BookingVIew, RoomDetailView
app_name='hotel'
urlpatterns = [
    path('room_list/', RoomListView, name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('booking_view/', BookingVIew.as_view(), name='booking_view'),
    path('room/<category>/', RoomDetailView.as_view(), name='RoomDetailView'),
]