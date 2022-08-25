from django.urls import path, include
from .views import UserAPIView, RoomAPIView, MessageAPIView, UserListView, UserEditView, index, room, \
    MessageListView, RoomDetail, RoomCreatedView, RoomListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserAPIView)
router.register(r'room', RoomAPIView)
router.register(r'message', MessageAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('<int:pk>/', UserView.as_view(), name='user_detail'),
    path('users', UserListView.as_view(), name='users'),
    path('<int:pk>/edit', UserEditView.as_view(), name='edit_user'),
    path('', index, name='chat'),
    path('<str:room_name>/', room, name='room'),   # путь для комнаты чата
    path('messages', MessageListView.as_view(), name='messages'),
    path('myroom/<int:pk>', RoomDetail.as_view(), name='roomm'),
    path('roomcreated', RoomCreatedView.as_view(), name='room_created'),
    path('rooms', RoomListView.as_view(), name='rooms')

]