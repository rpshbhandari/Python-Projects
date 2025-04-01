from django.db import models

class QuestionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice'),
        # ('TF', 'True/False'),
        # ('FIB', 'Fill in the Blanks'),
        # ('ESSAY', 'Essay'),
    ]

    text = models.TextField()
    category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
