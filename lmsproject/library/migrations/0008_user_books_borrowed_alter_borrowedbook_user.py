# Generated by Django 5.0.6 on 2024-07-30 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_borrowedbook_books_remove_borrowedbook_users_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='books_borrowed',
            field=models.ManyToManyField(related_name='users', to='library.book'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.user'),
        ),
    ]
