# Generated by Django 3.0.5 on 2020-07-09 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_poster', models.ImageField(upload_to='slide')),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.Movies')),
            ],
        ),
    ]