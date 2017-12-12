from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import validate_slug

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False) 
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SubmissionForm(forms.Form):
    submission = forms.CharField(
        max_length=50,
        validators=[validate_slug],
        required=True,
        widget=forms.TextInput(attrs={'size':'100', 'class':"large-6.columns"}))

class GroupForm(forms.ModelForm):
    Name = forms.CharField(
        max_length=50,
        validators=[validate_slug],
        required=True,
        widget=forms.TextInput(attrs={'size':'125', 'class':"large-6.columns"}))
    Description = forms.CharField(max_length=100,
        validators=[validate_slug],
        required=True,
        widget=forms.TextInput(attrs={'size':'120', 'class':"large-6.columns"}))
"""
    class Meta:
        model = Group
        fields = ('Group',)
"""
