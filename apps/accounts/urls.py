from django.urls import path
from .views import LoginView, RegisterView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('account/register/', RegisterView.as_view(), name='register'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
]
