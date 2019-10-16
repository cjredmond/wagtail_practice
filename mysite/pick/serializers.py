from .models import League, Team, Game, UserPick
from rest_framework import serializers
import json
from django.core import serializers as DjangoSerializers

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['TeamName', 'TeamLogo', 'leagues']

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['League', 'GameTime', 'HomeTeam', 'AwayTeam', 'HomeScore', 'AwayScore', 'GameCompleted', 'GameResult', 'Active']


class UserPickSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPick
        fields = ['User', 'Game', 'PickTime', 'UserPick', 'PickStatus']

class LeagueSerializer(serializers.ModelSerializer):
	# games = GameSerializer(many=True, read_only=True)
	games_list = serializers.SerializerMethodField()
	# games_list = GameSerializer(many=True)
	class Meta:
		model = League
		fields = ['LeagueName', 'LeagueCountry', 'LeagueLogo', 'International', 'games_list']
	def get_games_list(self, obj):
		return DjangoSerializers.serialize('json',list(obj.getActiveGames()))