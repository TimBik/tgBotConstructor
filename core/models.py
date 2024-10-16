from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class TgEvent(models.Model):
    class TgEventType(models.TextChoices):
        start_event = "START", "Start event"

    message = models.OneToOneField(
        to="core.Message",
        on_delete=models.PROTECT
    )

    type = models.CharField(
        choices=TgEventType.choices,
        default=None,
        max_length=20,
        null=True,
        blank=True,
    )


class Message(models.Model):
    pass


class InlineMessage(Message):
    image = models.ImageField(
        upload_to='images/inline_messages',
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name="создано"
    )
    modified = models.DateTimeField(
        default=timezone.now,
        verbose_name="обновлено"
    )

    class Meta:
        verbose_name = "инлайн сообщение бота"
        verbose_name_plural = "инлайн сообщения бота"


class InlineButton(models.Model):
    class InlineButtonType(models.TextChoices):
        next_inline_message = 'NEXT_INLINE_MESSAGE'
        next_bot_message = 'NEXT_BOT_MESSAGE'

    text = models.CharField(max_length=64)
    type = models.CharField(
        choices=InlineButtonType.choices,
        max_length=64,
        null=True,
        blank=True,
    )
    inline_message = models.ForeignKey(
        "core.InlineMessage",
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "инлайн кнопка"
        verbose_name_plural = "инлайн кнопки"


class BotMessage(Message):
    text = models.TextField(
        max_length=2048,
        verbose_name="текст",
        default="",
    )
    image = models.ImageField(
        upload_to='images/bot_messages',
        null=True,
        blank=True,
        default=None,
    )
    file = models.FileField(
        upload_to='files/bot_messages',
        null=True,
        blank=True,
        default=None,
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name="создано"
    )
    modified = models.DateTimeField(
        default=timezone.now,
        verbose_name="обновлено"
    )

    class Meta:
        verbose_name = "сообщение бота"
        verbose_name_plural = "сообщения бота"


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        AUTHORIZED = 'AUTHORIZED'
        ADMIN = 'ADMIN'
        ANONIM = 'ANONIM'

    tg_id = models.BigIntegerField(
        unique=True,
        verbose_name="id из тг",
    )
    role = models.CharField(
        max_length=20,
        choices=Role,
        default=Role.ANONIM,
        verbose_name="роль пользователя"
    )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
