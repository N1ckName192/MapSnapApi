from rest_framework import generics, status, permissions
from .models import Place, Review
from .serializers import PlaceSerializer, ReviewSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView

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
        place_id = self.kwargs['place_id']
        place = Place.objects.get(id=place_id)
        serializer.save(place=place)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "User registered successfully",
                "username": user.username,
                "token": token.key,
            },
            status=status.HTTP_201_CREATED
        )

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": "Login successful",
                    "username": user.username,
                    "api_key": token.key
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Invalid username or password"},
            status=status.HTTP_400_BAD_REQUEST
        )