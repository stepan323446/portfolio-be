from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectsListView.as_view()),
    path('<slug:slug>/', ProjectView.as_view())
]