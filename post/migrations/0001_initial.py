# Generated by Django 5.1.1 on 2024-09-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Post')),
                ('date_posted', models.DateField(verbose_name='DATE CREATED')),
            ],
        ),
    ]
