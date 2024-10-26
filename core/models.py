from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from model_utils.managers import InheritanceManager


class TgEventType(models.TextChoices):
    start_event = "START", "Start event"


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name="создано"
    )
    modified = models.DateTimeField(
        default=timezone.now,
        verbose_name="обновлено"
    )

    class Meta:
        abstract = True


class TgEvent(TimeStampedMixin):
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


class Message(TimeStampedMixin):
    objects = InheritanceManager()
    text = models.TextField(
        max_length=2048,
        verbose_name="текст",
        default="",
    )
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
        default=None,
    )


class InlineMessage(Message):
    class Meta:
        verbose_name = "инлайн сообщение бота"
        verbose_name_plural = "инлайн сообщения бота"


class InlineButton(models.Model):
    text = models.CharField(max_length=64)
    inline_message = models.ForeignKey(
        "core.InlineMessage",
        related_name="inline_buttons",
        null=True,
        on_delete=models.CASCADE
    )
    next_event = models.ForeignKey(
        "core.TgEvent",
        related_name="inline_buttons",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "инлайн кнопка"
        verbose_name_plural = "инлайн кнопки"

    def __str__(self):
        return self.text[:min(15, len(self.text))]


class BotMessage(Message):
    file = models.FileField(
        upload_to='files/bot_messages',
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        verbose_name = "сообщение бота"
        verbose_name_plural = "сообщения бота"

    def __str__(self):
        return self.text[:min(15, len(self.text))]


class Role(models.TextChoices):
    AUTHORIZED = 'AUTHORIZED'
    ADMIN = 'ADMIN'
    ANONIM = 'ANONIM'


class CustomUser(AbstractUser):
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
