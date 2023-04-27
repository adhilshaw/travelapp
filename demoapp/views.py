from operator import add

from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    teams = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'results': teams})
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#
#
# def substract(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     sub = x - y
#
#
# def division(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     div = x / y
#
#
# def multiplication(request, subtract=None):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     mul = x * y

# return render(request, "result.html", {'sum': add}, {'sub': subtract}, {'div': division}, {'mul': multiplication})
