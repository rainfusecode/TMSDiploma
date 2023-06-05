from django.urls import path
from .views import TaskList, Detail, TaskCreate, TaskUpdate, TaskDelete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', Detail.as_view(), name='detailtask'),
    path('createtask/', TaskCreate.as_view(), name='createtask'),
    path('updatetask/<int:pk>', TaskUpdate.as_view(), name='updatetask'),
    path('deletetask/<int:pk>', TaskDelete.as_view(), name='deletetask'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register')
]