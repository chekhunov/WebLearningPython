# Generated by Django 3.0.7 on 2020-06-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_name',
            field=models.CharField(default='example', max_length=100),
        ),
    ]