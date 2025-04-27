# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from drf.views import ItemViewSet

# router = routers.DefaultRouter()
# router.register(r'api/items', ItemViewSet, basename='item')
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
]