from flask import current_app
import time
import logging

from app import make_celery

celery = make_celery(current_app)


@celery.task()
def background_task(seconds):
    for x in range(0, seconds):
        print(str(x) + " seconds spent of " + str(seconds))
        time.sleep(1)
    return 42
