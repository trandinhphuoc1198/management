from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    path('<int:pk>',views.task_view,name='task-view')
]