# Generated by Django 2.1.7 on 2019-04-15 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchmodel',
            old_name='mealType',
            new_name='mealCategory',
        ),
        migrations.RemoveField(
            model_name='searchmodel',
            name='mealStyle',
        ),
    ]
