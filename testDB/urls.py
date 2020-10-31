from django.urls import path

from . import views
app_name = 'testDB'
urlpatterns = [
    path('', views.index, name='index'),
]