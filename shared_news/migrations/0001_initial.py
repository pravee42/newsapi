# Generated by Django 3.2.6 on 2021-11-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SharedNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(max_length=300)),
                ('source', models.CharField(max_length=700)),
                ('image', models.CharField(max_length=700)),
            ],
        ),
    ]
