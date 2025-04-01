from django.shortcuts import render, get_object_or_404
from .models import Question
from django.views.generic import ListView, DetailView


class QuestionListView(ListView):
    """Display a list of questions."""
    model = Question
    template_name = "questions/question_list.html"
    context_object_name = "questions"
    paginate_by = 10  # Number of questions per page

class QuestionDetailView(DetailView):
    """Display a single question."""
    model = Question
    template_name = "questions/question_detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = 'Some additional data'
        return context

