# Generated by Django 2.2 on 2020-10-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
