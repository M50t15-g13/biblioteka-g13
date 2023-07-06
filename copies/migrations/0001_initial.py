# Generated by Django 4.2.2 on 2023-07-05 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField()),
                ('state', models.CharField(choices=[('good', 'Good'), ('medium', 'Medium'), ('bad', 'Bad')], default='good', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_copies', to='books.book')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
