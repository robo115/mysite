# Generated by Django 4.1.7 on 2023-04-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='static/vendor/images/home/avatar.png', null=True, upload_to='users_images'),
        ),
    ]
