# Generated by Django 3.0.7 on 2020-06-26 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_name',
            new_name='name',
        ),
    ]
