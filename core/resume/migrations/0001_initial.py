# Generated by Django 3.0.3 on 2020-03-09 13:15

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(db_index=True, max_length=256, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=256)),
                ('message', models.TextField()),
                ('auther', models.CharField(max_length=128)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=254)),
                ('ISread', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('publish_status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
                ('auther', multiselectfield.db.fields.MultiSelectField(choices=[('H', 'hamed'), ('S', 'sahand')], max_length=3)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.CharField(db_index=True, max_length=128, unique=True)),
                ('tittle', models.CharField(db_index=True, max_length=256, unique_for_date='published_at')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('main_text', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', help_text='uplaod image', null=True, upload_to='post', width_field='width_field')),
                ('width_field', models.PositiveIntegerField(blank=True, default='1080', null=True)),
                ('height_field', models.PositiveIntegerField(blank=True, default='720', null=True)),
                ('main_file', models.FileField(blank=True, null=True, upload_to='resume_file')),
                ('category_list', models.ManyToManyField(to='resume.Category')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ['-published_at'],
            },
        ),
    ]
