from django.urls import path
from .views import question_list, question_detail

app_name = "questions"

urlpatterns = [
    path("", question_list, name="question_list"),
    path("<int:pk>/", question_detail, name="question_detail"),
]
