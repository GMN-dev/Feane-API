# Generated by Django 4.1.7 on 2023-03-05 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_menu_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
    ]