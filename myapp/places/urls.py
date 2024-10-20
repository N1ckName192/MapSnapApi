from django.urls import path
from .views import PlaceListCreateView, PlaceDetailView, ReviewCreateView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('places/', PlaceListCreateView.as_view(), name='place-list'),  # Маршрут для списка и создания мест
    path('places/<int:place_id>/', PlaceDetailView.as_view(), name='place-detail'),  # Маршрут для просмотра/редактирования места
    path('places/<int:place_id>/reviews/', ReviewCreateView.as_view(), name='review-create'),  # Маршрут для создания отзыва
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
