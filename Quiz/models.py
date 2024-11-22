from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)  # Overall user score
    
    def __str__(self):
        return self.user.username
    
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)  # e.g., Science, Math, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # To enable/disable the quiz

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(
        max_length=20,
        choices=[('MCQ', 'Multiple Choice'), ('TEXT', 'Text Answer')],
        default='MCQ'
    )

    def __str__(self):
        return f"{self.text} (Quiz: {self.quiz.title})"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} (Correct: {self.is_correct})"

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score})"

class Answer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    text_answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer to {self.question.text} in {self.attempt.quiz.title}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
