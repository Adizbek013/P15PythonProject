from aiogram.types import Message, FSInputFile
from celery import Celery

from web_scrapping import play

celery = Celery(
    'main',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)


@celery.task
def send_info():
    data = play()
    return data


celery.conf.beat_schedule = {
    'send_info': {
        'task': 'celery_app.send_info',
        'schedule': 10800.0
    }
}
