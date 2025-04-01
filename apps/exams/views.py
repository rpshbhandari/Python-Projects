from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Exam, ExamAttempt, ExamQuestion, ExamAnswer


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
    """Start an exam, logging the attempt and providing feedback."""
    
    def get(self, request, pk) -> HttpResponse:
        exam = get_object_or_404(Exam, pk=pk)

        # # Check if the exam is in the allowed time frame
        # if exam.start_time > timezone.now():
        #     messages.error(request, f"The exam '{exam.title}' has not started yet.")
        #     return redirect('exams:exam_detail', pk=exam.pk)  # Redirect to the exam details page
        
        # if exam.end_time < timezone.now():
        #     messages.error(request, f"The exam '{exam.title}' has already ended.")
        #     return redirect('exams:exam_detail', pk=exam.pk)  # Redirect to the exam details page

        # Log the user's attempt
        exam_attempt = ExamAttempt.objects.create(
            user=request.user,
            exam=exam,
            start_time=timezone.now()
        )

        # Redirect the user to the exam attempt page (or the first question, etc.)
        return redirect('exams:take_exam', pk=exam.pk)

class SubmitExamView(LoginRequiredMixin, View):
    """Submit an exam and calculate score (Dummy Implementation)."""

    def post(self, request, pk) -> HttpResponse:
        exam = get_object_or_404(Exam, pk=pk)
        score = 85  # Dummy score (Replace with actual score calculation logic)
        ExamAttempt.objects.create(user=request.user, exam=exam, score=score)
        return redirect("exams:exam_list")



class TakeExamView(LoginRequiredMixin, View):
    """Allow the user to answer questions for an exam."""
    
    def get(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)

        # Ensure exam is still active
        if exam.end_time and exam.end_time < timezone.now():
            messages.error(request, "The exam has ended.")
            return redirect('exams:exam_results', pk=exam.pk)

        # Get or create an exam attempt
        exam_attempt = ExamAttempt.objects.filter(user=request.user, exam=exam, end_time__isnull=True).first()
        if not exam_attempt:
            exam_attempt = ExamAttempt.objects.create(user=request.user, exam=exam, start_time=timezone.now())

        # Fetch all the questions related to the exam
        questions = ExamQuestion.objects.filter(exam=exam).order_by('id')

        # Paginate the questions (1 per page)
        paginator = Paginator(questions, 1)  # Show 1 question per page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context = {
            'exam': exam,
            'exam_attempt': exam_attempt,
            'page_obj': page_obj
        }
        
        return render(request, "exams/take_exam.html", context)  # ✅ FIXED

    def post(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        exam_attempt = get_object_or_404(ExamAttempt, user=request.user, exam=exam, end_time__isnull=True)

        # Get the current question
        question_id = request.POST.get('question_id')
        current_question = get_object_or_404(ExamQuestion, pk=question_id)

        user_answer = request.POST.get('answer_text')

        # Save the user's answer
        ExamAnswer.objects.create(
            attempt=exam_attempt,
            question=current_question,
            answer_text=user_answer,
            correct=self.check_answer(current_question, user_answer)  # Correctness check
        )

        # Get the next question
        next_question = ExamQuestion.objects.filter(exam=exam, id__gt=current_question.id).order_by('id').first()

        if next_question:
            # Redirect to the next question, maintaining pagination
            return redirect(f"{request.path}?page={next_question.id}")  # ✅ FIXED pagination

        else:
            # No more questions, mark the exam as completed
            exam_attempt.end_time = timezone.now()
            exam_attempt.save()
            messages.success(request, "You have completed the exam!")
            return redirect('exams:exam_results', pk=exam.pk)

    def check_answer(self, question, user_answer):
        """Check whether the user's answer is correct."""
        return user_answer.strip().lower() == question.correct_answer.strip().lower()  # ✅ Handles case sensitivity & whitespace
