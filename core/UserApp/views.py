from django.shortcuts import render

from UserApp.models import Player, PlayerLevel


def test(request):
    Player.objects.exclude(id=1)