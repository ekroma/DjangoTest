from django.db import models

class Room(models.Model):
    room_name = models.CharField('room_name',max_length=50)

    def __str__(self) -> str:
        return self.room_name


class User(models.Model):
    username = models.CharField('username', max_length=100)
    room_id = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL, 
        null=True,
        related_name='users'
    )

    def __str__(self) -> str:
        return f'{self.username}-{self.room_id}'


