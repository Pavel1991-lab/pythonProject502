# Generated by Django 4.2.5 on 2023-09-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images')),
                ('views', models.IntegerField(default=0)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
