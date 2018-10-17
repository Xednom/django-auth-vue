from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view

# Create your views here.


def public(request):
    return HttpResponse("You don't need to be authenticated to see this.")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated.")
