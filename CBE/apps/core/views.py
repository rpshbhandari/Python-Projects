from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def dispatch(self, request, *args: Any, **kwargs: Any) -> Any:
        """
        Redirect authenticated users to the home page.
        """
        if request.user.is_authenticated:
            return redirect('home:home')  # Replace 'home' with the name of your home URL pattern
        return super().dispatch(request, *args, **kwargs)

# About Page View
class AboutView(TemplateView):
    template_name = 'core/about.html'
    extra_context = {'title': 'About'}
