from django.urls import path,re_path
from . import views

urlpatterns = [
    path('meta-data',views.sync_meta_data),
    re_path(r'^task$',views.sync_task),
    re_path(r'^task/(?P<days>\d+)/$',views.sync_task)
]