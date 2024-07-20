from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# GET request for data to be printed to screen
@api_view(['GET'])
def get_data(request):
    data = [
        {'name': 'Item 1'},
        {'name': 'Item 2'},
        {'name': 'Item 3'},
    ]
    return Response(data)

# GET request for message to be printed to screen
@api_view(['GET'])
def get_message(request):
    message = "Hello from Django!"
    return Response(message)
