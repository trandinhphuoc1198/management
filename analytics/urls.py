from django.urls import path,include,re_path
from . import views

urlpatterns = [
    re_path(r'^project$',views.project_time_spent),
]
