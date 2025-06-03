from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet, KnoxLoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('auth/login/', KnoxLoginView.as_view(), name='knox_login'),
    #path('auth/login/', KnoxLoginView.as_view(), name='knox_login'),
]
