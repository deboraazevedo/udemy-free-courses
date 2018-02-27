import telegram

from django.http import HttpResponse
from django.conf import settings

from .utils import create_course, message
from .models import Course
from pyudemy import Udemy

 
def send_message(request):
    bot = telegram.Bot(token=settings.TOKEN)

    udemy = Udemy(settings.CLIENT_ID, settings.CLIENT_SECRET)

    course = udemy.courses(
                page=1, 
                page_size=1, 
                category='Development', 
                price='price-free', 
                ordering='newest'
            )

    kwargs = {
            'identifier': course['results'][0]['id'],
            'title': course['results'][0]['title'],
            'url': course['results'][0]['url'],
            'image_240x135': course['results'][0]['image_240x135'],
            'image_480x270': course['results'][0]['image_480x270']
        }

    if not Course.objects.filter(identifier=kwargs.get('identifier')):
        course = create_course(**kwargs)
        bot.send_message(chat_id="@freecoursesudemy", text=message(course), parse_mode=telegram.ParseMode.HTML)
    return HttpResponse()