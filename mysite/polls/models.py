from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    photo = models.ImageField(upload_to='question_photo', blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        date_now = timezone.now()
        return date_now >= self.pub_date >= date_now - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
