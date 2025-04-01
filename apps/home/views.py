from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm
from apps.exams.models import Exam  # Make sure to import the Exam model
from django.utils import timezone


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_exams'] = Exam.objects.filter(start_time__gte=timezone.now())
        return context

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'home/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context

# Edit Profile View
class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'home/edit_profile.html'
    success_url = reverse_lazy('home:profile')  # Redirect after successful edit

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)