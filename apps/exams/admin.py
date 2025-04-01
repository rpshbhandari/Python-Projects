# exams/admin.py
from django.contrib import admin
from .models import Exam, ExamQuestion, ExamAttempt

admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(ExamAttempt)
