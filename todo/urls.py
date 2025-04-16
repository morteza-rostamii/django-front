from django.urls import path
from . import views

urlpatterns = [
  
  # /todos (view)
  path('', views.index, name='index-view'),
  
  # update (view)
  path('update/<int:todo_id>', views.update, name='update-view'),
]
