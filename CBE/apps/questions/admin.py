from django.contrib import admin
from .models import QuestionCategory, Question, Choice

class ChoiceInline(admin.TabularInline):  # You can use `TabularInline` or `StackedInline`
    model = Choice
    extra = 3  # The number of empty choice forms to display initially (you can set it to 4 for 4 choices)
    fields = ['text', 'is_correct']  # The fields you want to display for the choices

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'question_type', 'created_at')
    search_fields = ('text',)
    list_filter = ('category', 'question_type')
    inlines = [ChoiceInline]  # Add the ChoiceInline to the Question admin

class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register models
admin.site.register(QuestionCategory, QuestionCategoryAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
