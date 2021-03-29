from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import UserRegistration, LogoutAPIView ,Login

urlpatterns = [
    path('login/', Login),
    path('logout/', csrf_exempt(LogoutAPIView.as_view())),
    path('register/', csrf_exempt(UserRegistration.as_view())),
]
