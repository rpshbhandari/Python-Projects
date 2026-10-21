from django.urls import path
from .views import QuestionListView, QuestionDetailView

app_name = "questions"

urlpatterns = [
    path("", QuestionListView.as_view(), name="question_list"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
]
