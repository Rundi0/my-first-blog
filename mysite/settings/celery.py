CELERY_BROKER_URL = 'redis://redis:6379//'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_ENABLE_UTC = True

CELERY_BEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler'