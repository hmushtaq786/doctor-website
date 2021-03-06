# Generated by Django 2.2.1 on 2020-05-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0010_auto_20200430_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_picture',
            field=models.ImageField(blank=True, default='blogs/blog_2.jpg', null=True, upload_to='blogs/', verbose_name='Blog picture'),
        ),
        migrations.AlterField(
            model_name='clienttestimonial',
            name='client_picture',
            field=models.ImageField(blank=True, default='blogs/default-client.png', upload_to='clients/', verbose_name='Client picture'),
        ),
    ]
