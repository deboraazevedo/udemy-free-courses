from django.db import models


class Course(models.Model):
    identifier = models.CharField('ID', max_length=100, unique=True)
    title = models.CharField('Published title', max_length=100)
    url = models.CharField('Url', max_length=100)
    image_240x135 = models.URLField('Image 240x135')
    image_480x270 = models.URLField('Image 480x270')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-pk']

