from django.forms import ModelForm
from django import forms
from .models import Project, Review


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


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {'value': 'Place your vote',
                  'body': 'Leave a comment'}

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs.update({'class': 'input'})
        self.fields['body'].widget.attrs.update({'class': 'input'})
