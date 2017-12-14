from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView                                                      
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm     
from django.contrib.auth.models import User
from django.utils.html import escape
from .forms import SubmissionForm
from .forms import GroupForm
from .models import submissions
from .models import Group
import datetime

import sys

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
#    form_class =  CreateUserForm #for email
    form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

def CreateGroupView(request):
    template_name = 'prj/group_create.html'

    #def get(self, request):
    if request.method == 'GET':
        form = GroupForm()
        users = User.objects.all()
        args = {'form': form, 'users': users}
        return render(request, template_name, args)

    #def post(self, request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['name']
            form = GroupForm()
            return redirect('other_groups')

        args = {'form': form, 'text': text}
        return render(request, template_name, args)
 
class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

def IndexView(request):
    template_name = 'prj/index.html'
    if request.method == 'GET':
        posts = Group.objects.all()
        args = {'posts': posts}
    return render(request, template_name, args)

def OtherGroupsView(request):
    template_name = 'prj/other_groups.html'
    if request.method == 'GET':
        posts = Group.objects.all().order_by('-created')
        args = {'posts': posts}
    return render(request, template_name, args)

class chat_view(TemplateView):
    template_name = 'prj/chat.html'

class LogInView(TemplateView):
    template_name = 'registration/login.html'



# Create your views here.
