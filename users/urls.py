from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ObtainToken, RegisterUser

# This handles the API url patterns for authentication
urlpatterns = [
    path("auth/login", ObtainToken.as_view()),
    path("auth/register", RegisterUser.as_view())
]
