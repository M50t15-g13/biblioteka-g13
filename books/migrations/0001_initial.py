# Generated by Django 4.2.2 on 2023-07-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=70)),
                ('pages_number', models.IntegerField()),
                ('publication_year', models.SmallIntegerField()),
                ('published_by', models.CharField(max_length=200)),
                ('img_url', models.URLField(max_length=250)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
