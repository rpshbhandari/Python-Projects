from django.urls import path
from .views import IndexView, HomeView,AboutView, ContactView, ServicesView, PrivacyPolicyView, TermsOfServiceView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('home/', HomeView.as_view(), name='home'),
]
