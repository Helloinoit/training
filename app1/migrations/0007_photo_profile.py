# Generated by Django 2.0.7 on 2018-07-13 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_photo_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Profile'),
        ),
    ]
