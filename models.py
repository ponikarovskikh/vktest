from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def accept(self):
        self.accepted = True
        self.save()

    def reject(self):
        self.delete()

    def __str__(self):
        return f"{self.from_user} to {self.to_user}: {'accepted' if self.accepted else 'not accepted'}"
