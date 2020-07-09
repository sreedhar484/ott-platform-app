# Generated by Django 3.0.5 on 2020-07-09 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('movie_poster', models.ImageField(upload_to='poster')),
                ('movie_long', models.ImageField(upload_to='long poster')),
                ('discription', models.TextField(default=None)),
                ('language', models.CharField(max_length=1000)),
                ('select_movie_types_liked', multiselectfield.db.fields.MultiSelectField(choices=[('horror', 'horror'), ('comedy', 'comedy'), ('thriller', 'thriller'), ('suspense', 'suspense'), ('romance', 'romance'), ('sci-fi', 'sci-fi'), ('drama', 'drama'), ('action', 'action')], max_length=59)),
                ('triler', models.FileField(default=None, upload_to='trailer')),
                ('movie', models.FileField(default=None, upload_to='movie')),
                ('hero_name', models.CharField(max_length=1000)),
                ('actor', models.ImageField(upload_to='hero')),
                ('heroin_name', models.CharField(max_length=1000)),
                ('actress', models.ImageField(upload_to='heroin')),
                ('director', models.ImageField(upload_to='director')),
                ('director_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.png', upload_to='pics')),
                ('m_type', multiselectfield.db.fields.MultiSelectField(choices=[('horror', 'horror'), ('comedy', 'comedy'), ('thriller', 'thriller'), ('suspense', 'suspense'), ('romance', 'romance'), ('sci-fi', 'sci-fi'), ('drama', 'drama'), ('action', 'action')], max_length=59)),
                ('favorate_hero', models.CharField(max_length=1000)),
                ('favorate_heroin', models.CharField(max_length=1000)),
                ('favorate_director', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
