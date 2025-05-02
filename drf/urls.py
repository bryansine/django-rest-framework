from django.urls import path, include
from rest_framework import routers
from .views import ItemViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('token-auth/', obtain_auth_token, name='api_token_auth'),

]