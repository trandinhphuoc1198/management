
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('top/',include('main.urls')),
    path('admin/', admin.site.urls),
    path('sync/',include('redmine.urls')),
    path('analytics/',include('analytics.urls')),
]
