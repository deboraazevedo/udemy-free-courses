import requests

from django.core.urlresolvers import reverse

from celery import task
from decouple import config


@task(ignore_result=True)
def search_course():
    requests.get(config('URL'))