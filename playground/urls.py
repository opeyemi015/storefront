from django.urls import path
from . import views
import playground

#URLConf
urlpatterns = [
    path('home/', views.say_hello)
]