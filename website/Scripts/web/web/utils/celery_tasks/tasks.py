import logging

from web.utils.celery_tasks.celery import app
import os, sys

logger  = logging.getLogger('django')
B_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, B_DIR)
sys.path.insert(0, os.path.join(B_DIR, 'apps'))
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setting.local')
from verifications.send import send_email_code


@app.task
def send_sms(send_to):
    try:
        result = send_email_code(send_to)
        return result

    except Exception as error:
        logger.error(error)


