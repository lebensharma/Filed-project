from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('create/<str:audioFileType>', views.create, name='create'),
    path('get/<str:audioFileType>/<int:audioFileID>', views.get, name='get'),
    path('delete/<str:audioFileType>/<int:audioFileID>', views.delete, name='delete'),
    # path('update', views.update, name='update'),
    # path('update', views.update, name='update'),
]