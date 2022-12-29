from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.project_time_spent),
    path('<int:person>',views.project_time_spent_by_person)
]
