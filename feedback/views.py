from rest_framework import generics as rest_generics
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from .serializers import MessageSerializer
import time

# Create your views here.
@extend_schema(tags=['Feedback'])
class CreateMessageView(rest_generics.CreateAPIView):
    serializer_class = MessageSerializer
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)