from django.conf import settings
from django.db import IntegrityError

from .models import Course

from pyudemy import Udemy


def create_course(**kwargs):
    if not Course.objects.filter(identifier=kwargs.get('identifier')):
        course = Course.objects.create(**kwargs)
    return course

def message(course):
    message = 'New course available! \n https://www.udemy.com{}'.format(course.url)
    return message


