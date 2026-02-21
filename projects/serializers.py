from rest_framework import serializers

from rest_framework import serializers
from .models import Project, Contributor, ProjectImage
from biography.serializers.nested import SkillSerializer

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "alt", "order"]


class ProjectListSerializer(serializers.ModelSerializer):
    primary_skills = SkillSerializer(many=True)
    contributors = ContributorSerializer(many=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'id', 
            'title', 
            'slug', 
            'subtitle', 
            'background', 
            
            'primary_skills', 
            'skills',

            'excerpt', 

            'status',
            'type',
            'role',
            
            'file',
            'code_url',
            'run_url',
            
            'contributors', 
            'images', 
            'is_favorite',

            'date_created',
            'date_completed'
        )

class ProjectSerializer(serializers.ModelSerializer):
    primary_skills = SkillSerializer(many=True)
    skills = SkillSerializer(many=True)
    contributors = ContributorSerializer(many=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'id', 
            'title', 
            'slug', 
            'subtitle', 
            'background', 
            
            'primary_skills', 
            'skills',

            'content', 
            'excerpt', 

            'status',
            'type',
            'role',

            'file',
            'code_url',
            'run_url',
            
            'contributors', 
            'images', 
            'is_favorite',

            'date_created',
            'date_completed'
        )