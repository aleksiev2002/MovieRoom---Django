# Generated by Django 4.1.3 on 2022-11-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('biography', models.TextField()),
                ('birthday', models.CharField(max_length=30)),
                ('deathday', models.CharField(max_length=30)),
                ('place_of_birth', models.CharField(max_length=100)),
            ],
        ),
    ]
