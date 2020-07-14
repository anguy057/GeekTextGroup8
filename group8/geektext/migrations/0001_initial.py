# Generated by Django 3.0.8 on 2020-07-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('number_sold', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
