# questions/admin.py
from django.contrib import admin
from .models import Question, QuestionCategory, Choice

admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Choice)
