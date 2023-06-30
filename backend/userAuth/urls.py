from django.contrib import admin
from django.urls import path,include
from userAuth.views import userAuthViewSet, CheckEmailViewSet, LoginViewSet
from rest_framework import routers
# from . import views


router = routers.DefaultRouter()
router.register(r'users', userAuthViewSet)
router.register(r'check-email', CheckEmailViewSet, basename='check-email')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    
    path("", include(router.urls))
    
]