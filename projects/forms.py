from .models import Project
import djhacker
from dal import autocomplete
from django import forms

djhacker.formfield(
    Project.primary_skills,
    forms.ModelMultipleChoiceField,
    widget = autocomplete.ModelSelect2Multiple(url='autocomplete-skills', attrs={'data-html': True})
)
djhacker.formfield(
    Project.skills,
    forms.ModelMultipleChoiceField,
    widget = autocomplete.ModelSelect2Multiple(url='autocomplete-skills', attrs={'data-html': True})
)