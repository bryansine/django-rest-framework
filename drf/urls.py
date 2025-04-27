# from django.contrib import admin


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
]