import djhacker
from .models import Skill, FileModel
from dal import autocomplete
from django import forms

# Djhacker
# https://github.com/yourlabs/djhacker
djhacker.formfield(
    Skill.cat,
    forms.ModelChoiceField,
    widget = autocomplete.ModelSelect2(url='autocomplete-skills-cats', attrs={'data-html': True})
)
djhacker.formfield(
    FileModel.cats,
    forms.ModelMultipleChoiceField,
    widget = autocomplete.ModelSelect2Multiple(url='autocomplete-skills-cats', attrs={'data-html': True})
)