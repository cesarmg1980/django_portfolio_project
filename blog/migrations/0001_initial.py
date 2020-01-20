# Generated by Django 3.0.2 on 2020-01-20 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='blog/images/')),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
