from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input'})
        self.fields['featured_image'].widget.attrs.update({'class': 'input'})
        self.fields['description'].widget.attrs.update({'class': 'input'})
        self.fields['demo_link'].widget.attrs.update({'class': 'input'})
        self.fields['source_link'].widget.attrs.update({'class': 'input'})
        self.fields['tags'].widget.attrs.update({'class': 'input'})
