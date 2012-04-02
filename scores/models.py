from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=200)

class Fixture(models.Model):
	date_played = models.DateTimeField('date played')
	player1 = models.ForeignKey(Player, related_name='player1')
	player2 = models.ForeignKey(Player, related_name='player2')