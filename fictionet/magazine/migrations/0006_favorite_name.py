# Generated by Django 3.2.12 on 2022-04-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='name',
            field=models.CharField(default='ew', max_length=200),
            preserve_default=False,
        ),
    ]
