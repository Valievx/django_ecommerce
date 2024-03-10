from django.contrib import admin
from chat.models import Chat, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'chat',
        'author',
        'get_recipient',
        'message',
        'pub_date'
    )

    def get_recipient(self, obj):
        chat = obj.chat

        members = chat.members.all()

        for member in members:
            if member != obj.author:
                return member
        return None

    get_recipient.short_description = 'Recipient'
