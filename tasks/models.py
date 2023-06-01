from django.db import models
import sys, os
sys.path.append(os.path.abspath('../accounts.models'))
from accounts.models import User
from django.urls import reverse

DEADLINE_CHOICES = (
    ('','Обозначить срок...'),
    ('Не срочно','Не срочно'),
    ('Срочно','Срочно'),
    ('Без срока','Без срока')
)

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст задачи')
    slug = models.SlugField(null=False, unique=False)
    date = models.DateField(blank=True, null=True)
    deadline = models.CharField(max_length=20, choices=DEADLINE_CHOICES, default="Обозначить срок...")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'