# Generated by Django 3.2.12 on 2022-04-06 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_favorite_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('name', 'story')},
        ),
    ]