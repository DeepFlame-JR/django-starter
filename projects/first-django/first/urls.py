from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),  # router, view, name
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),
]
