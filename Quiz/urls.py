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
    
]
