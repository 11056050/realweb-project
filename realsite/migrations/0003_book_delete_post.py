# Generated by Django 4.2.6 on 2023-10-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realsite', '0002_alter_post_options_rename_put_date_post_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booktitle', models.CharField(max_length=200)),
                ('picture', models.TextField()),
                ('info', models.TextField()),
                ('creator', models.TextField()),
                ('release', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]