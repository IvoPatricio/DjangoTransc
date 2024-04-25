from django.db import models

# Create your models here.

from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # hashed for security
    username = models.CharField(max_length=100)
    avatar = models.BinaryField(null=True)  # Blob field for avatar
    num_games_won = models.IntegerField(default=0)
    num_tournaments = models.IntegerField(default=0)
    num_tournaments_won = models.IntegerField(default=0)

class Friend_Requests(models.Model):
    id = models.AutoField(primary_key=True)
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    was_accepted = models.BooleanField(default=False)
    was_canceled = models.BooleanField(default=False)
    was_refused = models.BooleanField(default=False)

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    chat_room_id = models.IntegerField()
    sender_id = models.IntegerField()
    content = models.TextField()

class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    tournament_id = models.IntegerField(null=True)  # NULL if not a tournament game
    was_accepted = models.BooleanField(default=False)
    was_canceled = models.BooleanField(default=False)
    was_refused = models.BooleanField(default=False)
    has_finished = models.BooleanField(default=False)
    user1_score = models.IntegerField(default=0)
    user2_score = models.IntegerField(default=0)

class Chat_Rooms(models.Model):
    id = models.AutoField(primary_key=True)
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    was_blocked = models.BooleanField(default=False)
    block_user_id = models.IntegerField(null=True)  # User that issued block, NULL if not blocked

class Tournaments(models.Model):
    ID = models.AutoField(primary_key=True)
    creator_id = models.IntegerField()
    has_started = models.BooleanField(default=False)
    has_finished = models.BooleanField(default=False)

class Tournaments_Users(models.Model):
    ID = models.AutoField(primary_key=True)
    tournament_id = models.IntegerField()
    user_id = models.IntegerField()
    was_accepted = models.BooleanField(default=False)
    was_canceled = models.BooleanField(default=False)
    was_refused = models.BooleanField(default=False)
    position = models.IntegerField(default=0)  # 0 is for the winner
