# Generated by Django 4.1.7 on 2023-04-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='store.tag'),
        ),
    ]