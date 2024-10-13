from django.contrib import admin

from core.models import BotMessage, InlineMessage, InlineButton


@admin.register(BotMessage)
class BotMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(InlineMessage)
class InlineMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(InlineButton)
class InlineButtonAdmin(admin.ModelAdmin):
    pass