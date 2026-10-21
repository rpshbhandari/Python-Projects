from django.db import models
from django.contrib.auth.models import User
from apps.questions.models import Question
import random
from django.utils import timezone
from datetime import timedelta



def random_start_time():
    """Returns a random datetime within the last 120 minutes."""
    dt = timezone.now() - timedelta(minutes=random.randint(1, 120))

    print(f"Generated start_time: {dt} (Type: {type(dt)})")  # Debugging line
    return dt  

class Exam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, related_name="exam_questions", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exam.title} - {self.question.text[:30]}"

class ExamAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=random_start_time)

    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam.title} ({self.score})"

class ExamAnswer(models.Model):
    attempt = models.ForeignKey(ExamAttempt, related_name="answers", on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    answer_text = models.TextField()
    correct = models.BooleanField(default=False)