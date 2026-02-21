from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.safestring import mark_safe

# Create your models here.

class SkillCategory(models.Model):
    title       = models.CharField(max_length=150, verbose_name="Title")

    def __str__(self):
        return self.title


class Skill(models.Model):
    name        = models.CharField(max_length=150, verbose_name="Name")
    icon        = models.FileField(upload_to="icons/", blank=False)
    cat         = models.ForeignKey(SkillCategory, null=True, on_delete=models.SET_NULL, related_name='skills')
    is_filter   = models.BooleanField(default=True)

    icon_svg    = models.TextField(blank=True, null=True, verbose_name="Icon (svg code)")
    background  = models.CharField(max_length=50, blank=True, null=True, verbose_name="Background (hex)")

    def __str__(self) -> str:
        return self.name
    
    @property
    def get_icon_url(self):
        return self.icon.url
    
class PrimaryBio(models.Model):
    photo   = models.FileField(upload_to='files/')
    description = RichTextUploadingField()
    url_resume = models.URLField(null=True, blank=True)
    
class Contact(models.Model):
    name    = models.CharField(max_length=100)
    icon_svg = models.TextField()
    url     = models.CharField(max_length=100)
    order   = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Education(models.Model):
    name        = models.CharField(max_length=150, verbose_name="Education title (University name)")
    subname        = models.CharField(max_length=150, verbose_name="Your direction")
    icon        = models.FileField(upload_to="education/", blank=False)
    url         = models.CharField(max_length=100)
    content     = RichTextUploadingField(blank=True, verbose_name="Content")
    skills      = models.ManyToManyField(Skill, blank=True, verbose_name='Jobs')

    time_start  = models.DateField()
    time_end    = models.DateField(blank=True, null=True)

    document_name = models.CharField(max_length=25, default='Serificate')
    document    = models.FileField(upload_to="education/files/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Job(models.Model):
    name        = models.CharField(max_length=150, verbose_name="Job name")
    company     = models.CharField(max_length=150, verbose_name="Company")
    icon        = models.ImageField(upload_to="jobs/", blank=False)
    time_start  = models.DateField()
    time_end    = models.DateField(blank=True, null=True)
    content     = models.TextField()
    skills      = models.CharField(max_length=255, default='HTML • CSS • JavaScript')

    def __str__(self) -> str:
        return self.name
    
    @property
    def get_icon_url(self):
        return self.icon.url


class FolderModel(models.Model):
    COLOR = (
        ("green", "Green"),
        ("blue", "Blue"),
        ("yellow", "Yellow")
    )
    
    title       = models.CharField(max_length=150)
    colorType   = models.CharField(max_length=30, choices=COLOR)
    order       = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "Folder"
        verbose_name_plural = "Folders"

class FileModel(models.Model):
    TEXT_ALIGN  = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right')
    )
    FILE_TYPE = (
        ('default', 'Default'),
        ('image_page', 'Image page'),
    )

    title       = models.CharField(max_length=150, verbose_name="Title")
    slug        = models.SlugField(max_length=150, db_index=True, unique=True, verbose_name="Slug")
    content     = RichTextUploadingField(blank=True, verbose_name="Content")
    textAlign   = models.CharField(max_length=15, default='left', choices=TEXT_ALIGN)
    folder      = models.ForeignKey(FolderModel, null=True, blank=True, on_delete=models.SET_NULL)

    order       = models.IntegerField(default=0)
    file_type   = models.CharField(max_length=15, default='default', choices=FILE_TYPE)

    # for image page
    image       = models.ImageField(upload_to="files/", null=True, blank=True)
    button_text = models.CharField(max_length=30, blank=True, null=True)
    button_url  = models.CharField(max_length=70, blank=True, null=True)

    # for contact
    is_contact_file = models.BooleanField()

    cats        = models.ManyToManyField(SkillCategory, blank=True, verbose_name='Categories')
    jobs        = models.ManyToManyField(Job, blank=True, verbose_name='Jobs')
    projects    = models.ManyToManyField('projects.Project', blank=True, verbose_name='Projects')
    educations  = models.ManyToManyField(Education, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('aboutme:single', kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name        = "File"
        verbose_name_plural = "Files"
