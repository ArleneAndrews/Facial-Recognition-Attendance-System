# Generated by Django 2.1.1 on 2018-09-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('attendance', '0004_faceid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
