from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]