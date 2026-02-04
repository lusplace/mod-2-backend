from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ChatRoom(models.Model):
    room_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, unique=True)

    owner = models.ForeignKey(User, 
        related_name='owned_rooms',
        on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User, 
        related_name='chat_rooms',
        )
    
    def __str__(self):
        return self.room_name


# Create your models here.
class Message(models.Model):

    author = models.ForeignKey(User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    body_text = models.CharField(max_length=255)
    pub_date = models.DateField()

    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        body_short = f'{text[:8]}...' if len(self.body_text) > 8 else self.body_text 
        return f'{self.pub_date}_{self.chat_room.room_name}_{self.author.username}_{body_short}'

#https://stackoverflow.com/questions/33182092/django-rest-framework-serializing-many-to-many-field
