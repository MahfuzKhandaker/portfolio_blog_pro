# Generated by Django 3.2.5 on 2021-07-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'comments',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='images/')),
                ('image_caption', models.CharField(blank=True, max_length=125, null=True)),
                ('featured', models.BooleanField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('number_of_views', models.IntegerField(blank=True, default=0, null=True)),
                ('read_time', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'posts',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('slug', models.SlugField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name_plural': 'tags',
                'ordering': ['-name'],
            },
        ),
    ]
