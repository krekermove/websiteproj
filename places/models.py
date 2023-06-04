from django.db import models
import sys, os
sys.path.append(os.path.abspath('../accounts.models'))
from accounts.models import User
from django.urls import reverse

DEADLINE_CHOICES = (
    ('','Выбрать категорию...'),
    ('Где поесть','Где поесть'),
    ('Продукты','Продукты'),
    ('Банкоматы','Банкоматы')
)

class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')
    slug = models.SlugField(null=False, unique=False)
    date = models.DateField(blank=True, null=True)
    deadline = models.CharField(max_length=20, choices=DEADLINE_CHOICES, default="Выбрать категорию...")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place_detail', args=[str(self.id)])


    class Meta:
        verbose_name = 'Места'
        verbose_name_plural = 'Места'