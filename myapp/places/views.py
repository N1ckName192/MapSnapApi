from rest_framework import generics
from .models import Place, Review
from .serializers import PlaceSerializer, ReviewSerializer

# Представления для мест
class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_object(self):
        place_id = self.kwargs['place_id']
        return generics.get_object_or_404(Place, pk=place_id)


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        place_id = self.kwargs['place_id']  # Получаем id места из URL
        place = Place.objects.get(id=place_id)  # Получаем объект места
        serializer.save(place=place)  # Сохраняем отзыв с привязкой к месту
