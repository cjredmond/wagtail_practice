from django.shortcuts import render
from .models import League, Team, Game, UserPick
from rest_framework import viewsets
from .serializers import LeagueSerializer, TeamSerializer, GameSerializer, UserPickSerializer

class LeagueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class UserPickViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserPick.objects.all()
    serializer_class = UserPickSerializer