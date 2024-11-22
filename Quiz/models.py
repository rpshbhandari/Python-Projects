from pyclbr import Class
from django.db import models

# Create your models here.

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=50)
    quiz_description = models.CharField(max_length=2000)
    quiz_duration = models.IntegerField()
    quiz_questions = models.IntegerField()
    quiz_passing_marks = models.IntegerField()
    quiz_total_marks = models.IntegerField()
    quiz_created_by = models.CharField(max_length=50)
    quiz_created_on = models.DateTimeField(auto_now_add=True)
    quiz_updated_on = models.DateTimeField(auto_now=True)
    quiz_is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.quiz_name