# Generated by Django 4.1 on 2022-08-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='static/img/card/car-service.jpg', upload_to='pagination/media/img/card')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
            ],
        ),
    ]
