from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

tasks: list = []

# table headers
headers = ['id', 'title', 'description', 'completed', 'edit', "delete"]

# /todo (view)
def index(request: any) -> HttpResponse:

  context = {}
  context['welcome_message'] = 'Hello, world. You\'re at the todo index.'
  context['title'] = 'Todo'
  context['tasks'] = tasks
  context['headers'] = headers

  # handle POST
  if request.method == 'POST':
    # get the action (just an input)
    action = request.POST.get('action')

    print('** ac')
    # create a new task
    if action == 'create':
      title = request.POST.get('title')
      description = request.POST.get('description')
      completed = request.POST.get('completed')

      print(
        title,
        description,
        completed
      )

      new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'completed': completed
      }

      tasks.append(new_task)
      context['tasks'] = tasks

      return redirect('index-view')
    
    elif action == 'update':
      # convert to int for comparison
      id = int(request.POST.get('id'))
      title = request.POST.get('title')
      description = request.POST.get('description')
      # value: 'on' or None
      completed = request.POST.get('completed') == 'on'

      print(title, description, completed)
      for task in tasks:
        if task['id'] == id:
          task['title'] = title
          task['description'] = description
          task['completed'] = completed
      
      context['tasks'] = tasks
      return redirect('index-view')
    
    elif action == 'delete':
      id = int(request.POST.get('id'))

      for task in tasks:
        if task['id'] == id:
          tasks.remove(task)
      
      context['tasks'] = tasks
      return redirect('index-view')

  return render(request, 'todo/index.html', context)

# /todo/create/{id}
def create(request: any) -> HttpResponse:
  # access globals
  global tasks

  # index-view context
  context = {}
  context['title'] = 'Create'

  return render(request, 'todo/index.html', context)

# /todo/update/{id} (view)
def update(request: any, todo_id: int) -> HttpResponse:
  context = {}
  context['title'] = 'Update'

  # find the task
  for task in tasks:
    if task['id'] == todo_id:
      context['task'] = task
  
  return render(request, 'todo/edit.page.html', context)

