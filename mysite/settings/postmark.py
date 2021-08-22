import os

POSTMARK = {
    'TOKEN': os.environ['POSTMARK_API_KEY'],
    'TEST_MODE': False,
    'VERBOSITY': 0,
}
PM_API_KEY = os.environ['POSTMARK_API_KEY']
MAIL_ADDRESS = os.environ['POSTMARK_MAIL_ADDRESS']

EMAIL_HOST = 'smtp.postmarkapp.com'
EMAIL_HOST_USER = os.environ['POSTMARK_API_KEY']
EMAIL_HOST_PASSWORD = os.environ['POSTMARK_API_KEY']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
