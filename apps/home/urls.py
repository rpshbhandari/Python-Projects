from django.urls import path
from .views import ProfileView, EditProfileView

app_name = 'home'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
]