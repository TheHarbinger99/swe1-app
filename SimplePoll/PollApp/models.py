import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,  default=0 ,blank=True, null=True)
    choice_text = models.CharField(max_length=200, default=0 ,blank=True, null=True)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text