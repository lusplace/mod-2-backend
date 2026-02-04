from django.contrib import admin
from .models import ChatRoom, Message

# Register your models here.

class ChatRoomAdmin(admin.ModelAdmin):
    fields = ['room_name',
        'description',
        'owner',
        'members',
        ]
class MessageAdmin(admin.ModelAdmin):
    fields = ['author',
            'pub_date',
            'body_text',
            'chat_room',
            ]


admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
