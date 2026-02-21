from django.urls import path
from .views import *

urlpatterns = [
    path('skills/', SkillListView.as_view()),
    path('skill-categories/', SkillCategoryListView.as_view()),
    path('primary-info/', PrimaryInfoView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('files/<slug:slug>', FileView.as_view()),
    path('files/', FileListView.as_view()),

    path('autocomplete-skills/', SkillAutocomplete.as_view(), name='autocomplete-skills'),
    path('autocomplete-skill-cats/', SkillCategoryAutocomplete.as_view(), name='autocomplete-skills-cats'),
]