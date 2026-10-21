from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count



# Create your views here.

def home(request) -> HttpResponse:
    user = models.User.objects.all()
    return render(request, './home.html', {'user': user})

def login(request) -> HttpResponse:
    return render(request, './login.html')

def signup(request) -> HttpResponse:
    return render(request, './signup.html')

def quiz(request) -> HttpResponse:
    quiz_list = models.Quiz.objects.all()
    print(quiz_list)
    return render(request, './quiz_list.html', {'quiz_list': quiz_list})


def quiz_list(request):
    quizzes = models.Quiz.objects.filter(is_active=True).annotate(question_count=Count('questions'))
    quiz_list = models.Quiz.objects.all()
    print(quiz_list)
    return render(request, './quiz_list.html', {'quiz_list': quiz_list})


@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(models.Quiz, id=quiz_id, is_active=True)
    return render(request, 'quiz_detail.html', {'quiz': quiz})

@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(models.Quiz, id=quiz_id)
    
    # Check if the user already has an incomplete attempt
    attempt, created = models.Attempt.objects.get_or_create(user=request.user, quiz=quiz)
    
    if not created:
        # If an attempt exists, redirect to the quiz page
        return redirect('quiz_question', attempt_id=attempt.id)
    
    return redirect('quiz_question', attempt_id=attempt.id)

@login_required
def quiz_question(request, attempt_id):
    attempt = get_object_or_404(models.Attempt, id=attempt_id, user=request.user)
    answered_questions = attempt.answers.values_list('question_id', flat=True)
    question = attempt.quiz.questions.exclude(id__in=answered_questions).first()
    
    if not question:
        return redirect('quiz_result', attempt_id=attempt.id)

    return render(request, 'quiz_question.html', {'question': question, 'attempt': attempt})

@login_required
def submit_answer(request, attempt_id, question_id):
    attempt = get_object_or_404(models.Attempt, id=attempt_id, user=request.user)
    question = get_object_or_404(models.Question, id=question_id, quiz=attempt.quiz)

    if request.method == 'POST':
        if question.question_type == 'MCQ':
            choice_id = request.POST.get('choice')
            selected_choice = get_object_or_404(models.Choice, id=choice_id, question=question)
            models.Answer.objects.create(attempt=attempt, question=question, selected_choice=selected_choice)
            if selected_choice.is_correct:
                attempt.score += 1
                attempt.save()
        elif question.question_type == 'TEXT':
            text_answer = request.POST.get('answer')
            models.Answer.objects.create(attempt=attempt, question=question, text_answer=text_answer)

    return redirect('quiz_question', attempt_id=attempt.id)


@login_required
def quiz_result(request, attempt_id) -> HttpResponse:
    attempt = get_object_or_404(models.Attempt, id=attempt_id, user=request.user)
    answers = models.Answer.objects.filter(attempt=attempt)
    total_questions = attempt.quiz.questions.count()
    return render(request, 'quiz_result.html', {
        'attempt': attempt,
        'answers': answers,
        'total_questions': total_questions
    })

def leaderboard(request, quiz_id):
    quiz = get_object_or_404(models.Quiz, id=quiz_id)
    leaderboard = models.Attempt.objects.filter(quiz=quiz).order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'quiz': quiz, 'leaderboard': leaderboard})
