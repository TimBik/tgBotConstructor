# Generated by Django 5.1.2 on 2024-10-26 19:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_inlinebutton_next_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgevent',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='создано'),
        ),
        migrations.AddField(
            model_name='tgevent',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='обновлено'),
        ),
    ]