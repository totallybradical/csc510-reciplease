# Generated by Django 2.1.7 on 2019-04-21 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_auto_20190420_1405'),
        ('recommender', '0003_auto_20190421_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchmodel',
            name='ingredients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredients.UserIngredient'),
        ),
    ]