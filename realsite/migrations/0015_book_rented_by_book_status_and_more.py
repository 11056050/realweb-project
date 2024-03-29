# Generated by Django 5.0.1 on 2024-01-03 10:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realsite', '0014_book_available_copies'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rented_by',
            field=models.ManyToManyField(blank=True, related_name='rented_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Not Rented', 'Not Rented'), ('Rented', 'Rented')], default='Not Rented', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rented_books',
            field=models.ManyToManyField(blank=True, related_name='user_rented_books', to='realsite.book'),
        ),
    ]
