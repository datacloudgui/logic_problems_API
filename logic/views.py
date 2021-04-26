from django.shortcuts import render

#Dependencies to manage Json files
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

#Dependencies for api management
from rest_framework.decorators import api_view
from rest_framework import status

import os
import csv

#Importing the py files with the logic
from logic.pingpong import find_second_loser
from logic.password_finder import Password_finder
from logic.clean_keylog import clean_sequences


@api_view(['GET'])
def secondloser(request):
    """
    This view process the second loser problem (Ping Pong)
    Note: The default values are the requiered in the problem.
    """

    player1 = request.GET.get('player1', 17)
    player2 = request.GET.get('player2', 15)
    player3 = request.GET.get('player3', 10)

    try:
        #Send params to the logic function, return the second_loser_name (str) and lost_games (list)
        second_loser_name, lost_games = find_second_loser(int(player1), int(player2), int(player3))
    except ValueError:
        #Manage if some param cannot be converted to int.
        return JsonResponse('Please review the scores sended, scores must be numbers',
                                safe=False, status= status.HTTP_400_BAD_REQUEST)

    data = [{"second_loser_name": second_loser_name,
                "lost games": lost_games}]

    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

def password_finder(request):
    """
    This view process the Passwords problem, receive the .txt and process it.
    Note: A basic form is returned when a GET request is made.
    """

    #Dict to store the file content
    data = {}

    if request.method == "GET":
        #Return the form to upload de file
        return render(request, "upload_file.html", data)

    #Select the file obtained through the form
    key_file = request.FILES['key_file']

    if not key_file.name.endswith('.txt') and not key_file.name.endswith('.csv'):
        return JsonResponse('Please upload a CSV or TXT file',
                                safe=False, status= status.HTTP_400_BAD_REQUEST)

    #Decode and convert the file to a list of string
    data_set = key_file.read().decode('UTF-8')
    data_list = data_set.splitlines()

    #Obtaining stats of the file using pandas
    file_stats = clean_sequences(data_list)

    #Creating an instance of the Password_finder class with the data
    pass_finder = Password_finder(data_list)
    password = pass_finder.find_password()

    data = [{"The password is": password,
                "Process finished": pass_finder.status},
                {"File stats": file_stats}]

    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)


def index(request):
    """
    This view response with a basic HTML to test the project easily
    """

    if request.method == "GET":
        #Return the basic HTML index
        return render(request, "app_home.html")