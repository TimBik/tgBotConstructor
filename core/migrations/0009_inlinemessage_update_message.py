# Generated by Django 5.1.2 on 2024-11-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_botmessage_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlinemessage',
            name='update_message',
            field=models.BooleanField(default=True, help_text='обновить это сообщение при переходе', verbose_name='обновить сообщение'),
        ),
    ]
