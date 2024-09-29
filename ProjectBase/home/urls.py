from django.urls import path
from . import views
urlpatterns = [
    path('',views.reqHome),
    path('/homepage', views.reqHome)
]
