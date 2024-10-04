from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField, ReCaptchaV2Checkbox

from website.models import Category, Author, Testimonial


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
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class TestimonialCreateForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = [
            "author_full_name",
            "author_position",
            "author_company",
            "comment",
            "author_company_logo",
        ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}
    ))
    company = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Company'}
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message'}
    ))
    captcha = ReCaptchaField()
