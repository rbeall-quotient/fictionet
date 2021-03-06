# Generated by Django 3.2.12 on 2022-04-07 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0007_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
