from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    # path('<str:project>',views.project_view),
]