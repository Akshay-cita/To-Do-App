from django.urls import path
from . import views 

urlpatterns =[

	path('tasklist/',views.TaskList,name='tasklist'),
	path('taskdetail/<str:pk>/',views.TaskDetailView,name='taskdetail'),
	path('taskcreate/',views.TaskCreate,name='taskcreate'),
	path('taskupdate/<str:pk>/',views.TaskUpdate,name='taskupdate'),
	path('taskdelete/',views.TaskDelete,name='taskdelete'),


] 