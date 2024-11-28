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
        return obj.text[:min(20, len(obj.text))]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "limit_text",
    )
    search_fields = ('text',)

    def limit_text(self, obj):
        return obj.text[:min(20, len(obj.text))]


class InlineButtonInline(admin.TabularInline):  # или admin.StackedInline для вертикального отображения
    exclude = ["created", "modified"]
    model = InlineButton
    extra = 0  # Количество пустых форм для добавления новых кнопок


@admin.register(InlineMessage)
class InlineMessageAdmin(admin.ModelAdmin):
    inlines = [InlineButtonInline]
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
        return obj.text[:min(20, len(obj.text))]


@admin.register(InlineButton)
class InlineButtonAdmin(admin.ModelAdmin):
    list_display = ("id", "text",)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TgEvent)
class TgEventAdmin(admin.ModelAdmin):
    fields = (
        "message",
        "type",
    )
