import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['NAME_BD'],
        'USER': os.environ['USER_BD'],
        'PASSWORD': os.environ['PASSWORD_BD'],
        'HOST': os.environ['HOST_BD'],
        'PORT': 5432,
    }
}
