# Generated by Django 5.0.2 on 2024-02-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_picture',
            field=models.ImageField(upload_to='recipes'),
        ),
    ]