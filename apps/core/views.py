from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Home Page View
class IndexView(TemplateView):
    template_name = 'core/index.html'

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'
    login_url = '/accounts/login/'
    

# About Page View
class AboutView(TemplateView):
    template_name = 'core/about.html'
    extra_context = {'title': 'About'}
