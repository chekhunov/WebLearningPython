# Generated by Django 3.0.7 on 2020-07-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_departments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
    ]