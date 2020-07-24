from django.db import models


class User(models.Model):

    ADMIN = 'superadmin'
    PLAYER = 'player'
    ROLES = ((0, ADMIN), (1, PLAYER))
    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLES)
    team_id = models.IntegerField()


class Team(models.Model):

    token = models.CharField(max_length=50)
