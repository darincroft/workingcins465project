from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from prj.models import Group
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
    name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name your group here...',
        }
    ))
    description=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Describe what your group is about here...',
        }
    ))

    class Meta:
        model = Group
        fields = ('name', 'description')
