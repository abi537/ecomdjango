# Generated by Django 5.1.4 on 2025-01-19 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_ordereditem_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditem',
            name='size',
        ),
    ]
