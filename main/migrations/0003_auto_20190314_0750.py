# Generated by Django 2.1.7 on 2019-03-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190314_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='description_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='title_en_us',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='title_ru',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
