from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

web: gunicorn intern_project.wsgi --log-file -

