# Generated by Django 2.0.7 on 2018-08-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_text',
            field=models.CharField(blank=True, max_length=160),
        ),
    ]
