# Generated by Django 2.0.7 on 2018-07-11 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180710_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.Photo'),
        ),
    ]