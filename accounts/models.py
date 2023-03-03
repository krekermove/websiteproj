from django.db import models

class Users(models.Model):
	email = models.EmailField('Почта')
	password = models.CharField('Пароль', max_length=30)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
