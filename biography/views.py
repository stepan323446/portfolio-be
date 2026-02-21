from dal import autocomplete
from rest_framework import generics as rest_generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as rest_status
from drf_spectacular.utils import extend_schema

from .serializers.common import *
from .serializers.nested import *

# Create your views here.
@extend_schema(tags=['Skills'])
class SkillListView(rest_generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    pagination_class = None

@extend_schema(tags=['Skills'])
class SkillCategoryListView(rest_generics.ListAPIView):
    serializer_class = SkillCategorySerializer
    queryset = SkillCategory.objects.all()
    pagination_class = None

@extend_schema(tags=['Biography'])
class ContactView(rest_generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.order_by('order')
    pagination_class = None

@extend_schema(tags=['Biography'])
class FileView(rest_generics.RetrieveAPIView):
    serializer_class = FileSerializer
    queryset = FileModel.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

@extend_schema(
    tags=['Biography'], 
    request=None,
    responses=PrimaryInfoSerializer)
class PrimaryInfoView(APIView):
    def get(self, request, format=None):
        primaryBio = PrimaryBio.objects.first()
        #import time
        #time.sleep(3)
        if primaryBio == None:
            return Response({'error: Not found primary info'}, status=rest_status.HTTP_404_NOT_FOUND)
        
        primaryBioSerialized = PrimaryInfoSerializer(instance=primaryBio, context={'request': request})
        return Response(primaryBioSerialized.data)

@extend_schema(tags=['Biography'])
class FileListView(rest_generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = FileModel.objects.order_by('order')
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

# django-autocomplete-light
# https://django-autocomplete-light.readthedocs.io/en/master/
class SkillAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
    
class SkillCategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SkillCategory.objects.none()

        qs = SkillCategory.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs