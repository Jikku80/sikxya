# Generated by Django 3.2.4 on 2021-07-06 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
