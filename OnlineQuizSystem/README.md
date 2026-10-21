# Online Quiz System

A quiz site in Django. Users sign up, pick a quiz, answer its questions one at a time, and see their result and the quiz's leaderboard.

## Run it

```bash
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Add quizzes, questions and choices in the admin at `/admin/`. Set `DJANGO_SECRET_KEY` before running it anywhere but your own machine.
