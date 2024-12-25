from django import forms
from .models import *


class CourseForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label=""
    )


class LessonForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label=""
    )

    homework = forms.CharField(
        widget=forms.Textarea({
            'placeholder': "Uyga vazifani kiriting",
            'class': "form-control"
        }),
        label=""
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput({
            'class': 'form-control',
            'type': "datetime-local"
        }),
        input_formats=['%d.%m.%Y %H:%M'],
        label="",
        required=False
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select({
            'class': "form-select"
        }),
        label=""
    )
