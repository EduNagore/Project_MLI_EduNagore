# Generated by Django 4.2.1 on 2023-05-15 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_favorites'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorites',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Favorites'},
        ),
    ]
