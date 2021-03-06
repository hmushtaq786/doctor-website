# Generated by Django 2.2.5 on 2020-04-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0002_auto_20200428_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=50, verbose_name='Client name')),
                ('client_testimonial', models.TextField(blank=True, verbose_name='Client testimonial')),
                ('client_picture', models.ImageField(blank=True, upload_to='', verbose_name='Client picture')),
            ],
        ),
    ]
