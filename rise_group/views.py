from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# /
def index(request: any) -> HttpResponse:
  return render(request, 'rise_group/index.html')