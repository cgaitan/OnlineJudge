# Generated by Django 2.1.7 on 2019-03-26 02:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0009_auto_20180501_0436'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='acmcontestrank',
            unique_together={('user', 'contest')},
        ),
        migrations.AlterUniqueTogether(
            name='oicontestrank',
            unique_together={('user', 'contest')},
        ),
    ]