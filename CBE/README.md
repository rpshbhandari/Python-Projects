# CBE

An online exam site in Django. Users register and log in, keep a profile with a picture, and take timed exams built from a question bank of categorised multiple-choice questions.

## Run it

```bash
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Add questions and exams in the admin at `/admin/`. Set `DJANGO_SECRET_KEY` before running it anywhere but your own machine.
