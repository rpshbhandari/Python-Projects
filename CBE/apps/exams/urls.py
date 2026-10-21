from django.urls import path
from .views import ExamListView, ExamDetailView, StartExamView, SubmitExamView, TakeExamView

app_name = "exams"

urlpatterns = [
    path("", ExamListView.as_view(), name="exam_list"),
    path("<int:pk>/", ExamDetailView.as_view(), name="exam_detail"),
    path("<int:pk>/start/", StartExamView.as_view(), name="start_exam"),
    path("<int:pk>/submit/", SubmitExamView.as_view(), name="submit_exam"),
    path('exam/<int:pk>/take/', TakeExamView.as_view(), name='take_exam'),

]
