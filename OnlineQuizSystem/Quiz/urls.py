from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('quiz/', views.quiz, name='quiz'),
    # path('quiz/<str:quiz_name>/', views.quiz, name='quiz'),
    # path('quiz/<str:quiz_name>/question/<int:question_id>/', views.question, name='question'),
    # path('quiz/<str:quiz_name>/question/<int:question_id>/submit/', views.submit, name='submit'),
    # path('quiz/<str:quiz_name>/result/', views.result, name='result'),
    # path('quiz/<str:quiz_name>/leaderboard/', views.leaderboard, name='leaderboard'),
    path('quiz/list/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),
    path('attempt/<int:attempt_id>/question/', views.quiz_question, name='quiz_question'),
    path('attempt/<int:attempt_id>/question/<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
    path('attempt/<int:attempt_id>/result/', views.quiz_result, name='quiz_result'),
    path('quiz/<int:quiz_id>/leaderboard/', views.leaderboard, name='leaderboard'),
]
