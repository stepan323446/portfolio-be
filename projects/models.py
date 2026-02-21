from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from biography.models import Skill

# Create your models here.
class Contributor(models.Model):
    name        = models.CharField(max_length=150)
    url         = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    avatar      = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.name
    

class Project(models.Model):
    class ProjectType(models.TextChoices):
        COMMERCIAL = 'commercial', 'Commercial',
        PET = 'pet', 'Pet Project',
        OpenSource = 'open_source', 'Open Source',
        StartUp = 'startup', 'Start Up'

    class ProjectStatus(models.TextChoices):
        PLANNING = 'planning', 'Planning',
        IN_PROGRESS = 'in_progress', 'In Progress',
        REALESED = 'realesed', 'Realesed',
        ARCHIVE = 'archive', 'Archive'

    title       = models.CharField(max_length=150, verbose_name="Title")
    slug        = models.SlugField(max_length=150, db_index=True, unique=True, verbose_name="Slug")
    subtitle        = models.CharField(max_length=150, verbose_name="Type project")
    date_created = models.DateField()
    date_completed = models.DateField(blank=True, null=True)
    background  = models.ImageField(upload_to="uploads/")
    content     = RichTextUploadingField(blank=True, verbose_name="Content")
    excerpt     = models.TextField(blank=True, null=True)

    status      = models.CharField(max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.REALESED)
    type        = models.CharField(max_length=100, choices=ProjectType.choices, default=ProjectType.PET)
    role        = models.CharField(max_length=100, null=True, blank=True)

    primary_skills = models.ManyToManyField(Skill, related_name="primary_skills")
    skills      = models.ManyToManyField(Skill, verbose_name="Skills")
    
    is_favorite = models.BooleanField(default=False)

    file    = models.CharField(max_length=255, null=True, blank=True, verbose_name="File (name|url)")
    code_url    = models.CharField(max_length=150, null=True, blank=True, verbose_name="View code URL")
    run_url     = models.CharField(max_length=150, null=True, blank=True, verbose_name="Run URL")

    contributors = models.ManyToManyField(Contributor, blank=True)

    @property
    def get_photo_url(self):
        return self.background.url

    def __str__(self):
       return self.title
    
class ProjectImage(models.Model):
    product = models.ForeignKey(
        Project,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="projects/")
    alt = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Image for {self.product.title}"
    
class Redirect(models.Model):
    name        = models.CharField(max_length=150)
    url         = models.URLField()

    def __str__(self) -> str:
        return self.name