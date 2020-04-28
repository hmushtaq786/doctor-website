# Generated by Django 2.2.5 on 2020-04-28 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor_app', '0003_clienttestimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=100, verbose_name='Question')),
                ('answer', models.TextField(blank=True, verbose_name='Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_heading', models.CharField(blank=True, max_length=40, verbose_name='Service heading')),
                ('service_description', models.TextField(blank=True, verbose_name='Service description')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(blank=True, max_length=50, verbose_name='Blog title')),
                ('blog_topic', models.CharField(blank=True, max_length=20, verbose_name='Blog topic')),
                ('blog_content', models.TextField(blank=True, verbose_name='Blog content')),
                ('blog_picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Blog picture')),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('blog_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Blog author')),
            ],
        ),
    ]
