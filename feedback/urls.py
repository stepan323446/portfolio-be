from django.urls import path
from .views import *

urlpatterns = [
    path('send-message/', CreateMessageView.as_view()),
]