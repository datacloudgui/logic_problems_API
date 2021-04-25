from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from rest_framework import status

from logic.pingpong import find_second_loser



@api_view(['GET'])
def secondloser(request):

    player1 = request.GET.get('player1', 17)
    player2 = request.GET.get('player2', 15)
    player3 = request.GET.get('player3', 10)

    second_loser_name, lost_games = find_second_loser(player1, player2, player3)

    data = [{"second_loser_name": second_loser_name,
                "lost games": lost_games}]

    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)