# Generated by Django 5.1.2 on 2024-10-13 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InlineButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('NEXT_INLINE_MESSAGE', 'Next Inline Message'), ('NEXT_BOT_MESSAGE', 'Next Bot Message')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='InlineMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('buttons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inlinebutton')),
            ],
            options={
                'verbose_name': 'сообщение бота',
                'verbose_name_plural': 'сообщения бота',
            },
        ),
    ]
