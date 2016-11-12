from django.shortcuts import render
from django.http import HttpResponse

with open('../index.html', 'r') as fh:
    home_html = fh.read()

def home(request):
    return HttpResponse(home_html)
