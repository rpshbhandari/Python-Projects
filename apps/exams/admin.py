from django.contrib import admin
from .models import Exam, ExamQuestion, ExamAttempt

# Inline admin for adding ExamQuestions directly within Exam
class ExamQuestionInline(admin.TabularInline):
    model = ExamQuestion
    extra = 1  # Number of empty forms to display

class ExamAdmin(admin.ModelAdmin):
    inlines = [ExamQuestionInline]

# Registering the models
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamQuestion)
admin.site.register(ExamAttempt)
