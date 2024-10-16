from django.contrib import admin

from core.models import BotMessage, InlineMessage, InlineButton, CustomUser, TgEvent


@admin.register(BotMessage)
class BotMessageAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        'modified',
    )


@admin.register(InlineMessage)
class InlineMessageAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        'modified',
    )


@admin.register(InlineButton)
class InlineButtonAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TgEvent)
class TgEventAdmin(admin.ModelAdmin):
    pass
