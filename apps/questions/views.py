from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Question, QuestionCategory

def question_list(request):
    """Display all questions."""
    questions = Question.objects.all()
    return render(request, "questions/question_list.html", {"questions": questions})

def question_detail(request, pk):
    """Display a single question."""
    question = get_object_or_404(Question, pk=pk)
    return render(request, "questions/question_detail.html", {"question": question})
