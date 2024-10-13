from django.db import models


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

class InlineMessage(models.Model):
    # image = models.ImageField(
    #     upload_to=''
    # )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="создано"
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="обновлено"
    )

    class Meta:
        verbose_name = "инлайн сообщение бота"
        verbose_name_plural = "инлайн сообщения бота"


class BotMessage(models.Model):
    text = models.TextField(
        max_length=2048,
        verbose_name="текст"
    )
    # image = models.ImageField(
    #     upload_to=''
    # )
    # file = models.FileField(
    #
    # )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="создано"
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="обновлено"
    )

    class Meta:
        verbose_name = "сообщение бота"
        verbose_name_plural = "сообщения бота"
