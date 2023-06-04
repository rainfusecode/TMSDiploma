from django.urls import path
from .views import TaskList, Detail,TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', Detail.as_view(), name='detailtask'),
    path('createtask/', TaskCreate.as_view(), name = 'createtask'),
]