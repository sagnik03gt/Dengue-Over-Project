# Generated by Django 4.2.2 on 2023-10-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DENGUE_APP', '0002_alter_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_img',
            field=models.ImageField(default='default_news_image.jpg', upload_to='news_img/'),
        ),
    ]
