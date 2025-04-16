from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request: any) -> HttpResponse:
  # return HttpResponse("Hello, world. You're at the core index.")

  context = {
    'title': 'Core',
    'welcome_message': 'Hello, world. You\'re at the core index.',
    'users': [
      {'name': 'John', 'age': 25, 'is_active': True},
      {'name': 'Jane', 'age': 30, 'is_active': False},
      {'name': 'Bob', 'age': 35, 'is_active': True},
    ]
  }

  return render(request, 'core/index.html', context)

def about(request: any) -> HttpResponse:
  return render(request, 'core/about.html')

# /users
def users(request: any) -> HttpResponse:
  if request.method == 'POST':
    data = request.POST.get('name')
    return HttpResponse(f"posted: ** {data} **")  
  
  # GET: returns a template
  return render(request, 'core/users.html')