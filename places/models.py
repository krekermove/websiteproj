from django.db import models
import sys, os
sys.path.append(os.path.abspath('../accounts.models'))
from accounts.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator

DEADLINE_CHOICES = (
    ('','Выбрать категорию...'),
    ('Где поесть','Где поесть'),
    ('Продукты','Продукты'),
    ('Банкоматы','Банкоматы')
)

class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание', max_length=300)
    slug = models.SlugField(null=False, unique=False)
    date = models.DateField(blank=True, null=True)
    deadline = models.CharField(max_length=20, choices=DEADLINE_CHOICES, default="Выбрать категорию...")
    lattitude = models.FloatField('Широта',max_length=20,validators=[MinValueValidator(59.8),MaxValueValidator(60)])
    longtitude = models.FloatField('Долгота',max_length=20,validators=[MinValueValidator(30.147),MaxValueValidator(30.556)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place_detail', args=[str(self.id)])


    class Meta:
        verbose_name = 'Места'
        verbose_name_plural = 'Места'