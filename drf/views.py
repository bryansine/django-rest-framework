from .models import Item
from knox.models import AuthToken
from rest_framework import status
from django.contrib.auth import login
from .serializers import ItemSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class KnoxLoginView(APIView):
    serializer_class = AuthTokenSerializer
    permission_classes = []

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token[1],
            "expiry": token[0].expiry
        })
        

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [AllowAny, IsAuthenticated, IsAdminOrReadOnly, IsAdminUser, IsAuthenticatedOrReadOnly]