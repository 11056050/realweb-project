# Generated by Django 4.2.6 on 2023-11-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realsite', '0010_rename_title_chapter_ctitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='title',
            field=models.CharField(default='Chapter 1', max_length=255),
            preserve_default=False,
        ),
    ]
