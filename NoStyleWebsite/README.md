# NoStyleWebsite

A Django site with no CSS: a list of posts on the home page and a page for each post.

## Run it

```bash
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Add posts in the admin at `/admin/`. Set `DJANGO_SECRET_KEY` before running it anywhere but your own machine.
