# Generated by Django 4.1.7 on 2023-03-07 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_menu_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='menu',
            name='tag',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='api.tag'),
            preserve_default=False,
        ),
    ]
