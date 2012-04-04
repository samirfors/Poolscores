from django.db import models

class Tournament(models.Model):
	date_played = models.DateTimeField('date played')
	def __unicode__(self):
		return self.date_played

class Player(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__ (self):
		return self.name

class Fixture(models.Model):
	tournament = models.ForeignKey(Tournament)
	player1 = models.ForeignKey(Player, related_name='player1')
	player2 = models.ForeignKey(Player, related_name='player2')
	game = 'player1 - player2'
	def __unicode__(self):
		return self.game

class Winner(models.Model):
	fixture = models.ForeignKey(Fixture)
	winner = models.ForeignKey(Player)
	fpoints = models.IntegerField('f-points')
	def __unicode__(self):
		return self.winner