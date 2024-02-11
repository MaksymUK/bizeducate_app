from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth.forms import UserCreationForm

from website.models import Category, Author


class CourseSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="",
        empty_label="Select category",
    )
    city = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by city"}),
    )


class AuthorCreateForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ["username", "email", "password1", "password2",
                  "first_name", "last_name", "company", "position", "company_logo"]