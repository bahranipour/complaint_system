from django.urls import path
from .views import signup, user_login, user_logout,custom_password_change

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('password-change/', custom_password_change, name='custom_password_change'),
]