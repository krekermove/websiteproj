# Generated by Django 4.1.7 on 2023-06-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_tasks_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='deadline',
            field=models.CharField(choices=[('', 'Обозначить срок...'), ('Не срочно', 'Не срочно'), ('Срочно', 'Срочно'), ('Без срока', 'Без срока')], default='Обозначить срок...', max_length=20),
        ),
    ]
