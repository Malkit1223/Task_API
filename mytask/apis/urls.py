from django.urls import path
from taskapp.views import *
urlpatterns = [
    path('tasks/',TaskAPI.as_view()),
    path('tasks/<int:id>',TaskAPI.as_view())
  

]