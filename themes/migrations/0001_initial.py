# Generated by Django 4.2.7 on 2023-12-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('attrs', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
    ]
