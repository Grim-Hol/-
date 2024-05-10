from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

STATUS_CHOICES = [('d', 'Delete'), ('ip','in_process'),('p','Published')]

class Articles(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=25, blank=True)
    body = models.TextField(max_length=20000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    data_reverse = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'News {self.title}'

    def get_absolute_url(self):
        return reverse('body_txt', kwargs={'post_id':self.pk})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['data_reverse']


class Comment(models.Model):

    articles = models.ForeignKey('Articles', on_delete=models.CASCADE)
    author = models.CharField(default='any_user', max_length=25)
    main_text = models.TextField(max_length=1000)

    def __str__(self):
        return self.author, self.main_text