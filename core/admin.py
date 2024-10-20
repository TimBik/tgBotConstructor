from django.contrib import admin

from core.models import BotMessage, InlineMessage, InlineButton, CustomUser, TgEvent, Message


@admin.register(BotMessage)
class BotMessageAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        "id",
        "limit_text",
    )
    readonly_fields = (
        'created',
        'modified',
    )

    def limit_text(self, obj):
        return obj.text[:min(15, len(obj.text))]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "limit_text",
    )
    search_fields = ('text',)
    readonly_fields = (
        'created',
        'modified',
    )
    def limit_text(self, obj):
        return obj.text[:min(15, len(obj.text))]


@admin.register(InlineMessage)
class InlineMessageAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = (
        "id",
        "limit_text",
    )
    readonly_fields = (
        'created',
        'modified',
    )

    def limit_text(self, obj):
        return obj.text[:min(15, len(obj.text))]


@admin.register(InlineButton)
class InlineButtonAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TgEvent)
class TgEventAdmin(admin.ModelAdmin):
    pass
