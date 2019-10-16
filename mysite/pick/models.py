from django.db import models
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User

from django.core import serializers

@register_snippet
class League(models.Model):
	LeagueName = models.CharField(max_length=100, default='')
	LeagueCountry = models.CharField(max_length=50, default='')
	LeagueLogo = models.FileField(null=True, blank=True) 
	International = models.BooleanField(default=False)

	def __str__(self):
		return self.LeagueName

	def getActiveGames(self):
		# return serializers.serialize("json", self.game_set.all())
		return json.loads(self.game_set.all())

	@property
	def image_url(self):
		if self.LeagueLogo:
			return self.LeagueLogo.url
		return 'http://pccweb.ca/standrewsdresden/files/2016/03/Question-mark.png'


@register_snippet
class Team(models.Model):
	TeamName = models.CharField(max_length=100, default='')
	TeamLogo = models.FileField()
	leagues = models.ManyToManyField(League)

	def __str__(self):
		return self.TeamName

RESULT_CHOICES = [('home', 'home'), ('away', 'away'), ('draw', 'draw')]
RESULT_STATUS = [('win', 'win'), ('loss', 'loss'), ('submitted', 'submitted'), ('waiting', 'waiting')]

@register_snippet
class Game(models.Model):
	League = models.ForeignKey(League, on_delete=models.PROTECT)
	GameTime = models.DateTimeField(auto_now=False, auto_now_add=False)
	HomeTeam = models.ForeignKey(Team, related_name='HomeTeam', on_delete=models.PROTECT)
	AwayTeam = models.ForeignKey(Team, related_name='AwayTeam', on_delete=models.PROTECT)
	HomeScore = models.IntegerField(default=0)
	AwayScore = models.IntegerField(default=0)
	GameCompleted = models.BooleanField(default=False)
	GameResult = models.CharField(choices=RESULT_CHOICES, max_length=10, null=True, blank=True)
	Active = models.BooleanField(default=True)

@register_snippet
class UserPick(models.Model):
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	Game = models.ForeignKey(Game, on_delete=models.CASCADE)
	PickTime = models.DateTimeField(auto_now=False, auto_now_add=False)
	UserPick = models.CharField(choices=RESULT_CHOICES, max_length=10)
	PickStatus = models.CharField(choices=RESULT_STATUS, max_length=10)
