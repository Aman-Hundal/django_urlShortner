#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoshortner.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


#create templates folder -> go to settings of project folder, temapltes and adjust DIRS to templates -> create urls.py in your app folder -> create urlpatterns for app (start with index) -> go to views.py in app to create index function to manage index logci (render the index page) -> go to urls.py in project folder and include the apps urlpattern (import include and include(app.urls))
# setup db and models -> create the model in models.py -> adjust the settings file in project folder (installed apps section) and add the name of your app here -> run makemigration -> run migrate -> (create super user?) go to admin file in project folder and register your model (admin.site.register(URL))
#repeat  and create as many models, view functions, urlpatterns (in app) and html templates as you need. 