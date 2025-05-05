from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated, IsAdminOrReadOnly, AllowAny, IsAdminUser
from rest_framework.permissions import DjangoModelPermissions

from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [DjangoModelPermissions]
    #permission_classes = [AllowAny, IsAuthenticated, IsAdminOrReadOnly, IsAdminUser]
