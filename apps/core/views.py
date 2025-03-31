from django.shortcuts import render
from django.views.generic import TemplateView

# Home Page View
class IndexView(TemplateView):
    template_name = 'core/index.html'

class HomeView(TemplateView):
    template_name = 'core/home.html'

# About Page View
class AboutView(TemplateView):
    template_name = 'core/about.html'

# Contact Page View
class ContactView(TemplateView):
    template_name = 'core/contact.html'

# Services Page View
class ServicesView(TemplateView):
    template_name = 'core/services.html'

# Privacy Policy Page View
class PrivacyPolicyView(TemplateView):
    template_name = 'core/privacy_policy.html'

# Terms of Service Page View
class TermsOfServiceView(TemplateView):
    template_name = 'core/terms_of_service.html'
