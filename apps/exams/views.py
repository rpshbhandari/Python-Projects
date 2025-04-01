from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from .models import Exam, ExamAttempt

class ExamListView(LoginRequiredMixin, ListView):
    """Display all active exams."""
    model = Exam
    template_name = "exams/exam_list.html"
    context_object_name = "exams"

    def get_queryset(self):
        return Exam.objects.filter(is_active=True)

class ExamDetailView(LoginRequiredMixin, DetailView):
    """Display details of a single exam."""
    model = Exam
    template_name = "exams/exam_detail.html"
    context_object_name = "exam"

class StartExamView(LoginRequiredMixin, View):
    """Start an exam (Dummy Implementation)."""
    
    def get(self, request, pk) -> HttpResponse:
        exam = get_object_or_404(Exam, pk=pk)
        return HttpResponse(f"Exam '{exam.title}' started!")

class SubmitExamView(LoginRequiredMixin, View):
    """Submit an exam and calculate score (Dummy Implementation)."""

    def post(self, request, pk) -> HttpResponse:
        exam = get_object_or_404(Exam, pk=pk)
        score = 85  # Dummy score (Replace with actual score calculation logic)
        ExamAttempt.objects.create(user=request.user, exam=exam, score=score)
        return redirect("exams:exam_list")
