from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView                                                      
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.forms import UserCreationForm     
from django.utils.html import escape
from .forms import SubmissionForm
from .forms import GroupForm
from .models import submissions
import datetime

import sys

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
#    form_class =  CreateUserForm #for email
    form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

def CreateGroupView(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            return render(request, 'prj/group_create.html', {'form': form})
            
            #form.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        #form = GroupForm()
        #groups = Group.objects.order_by('-pub_date')
    return render(request, 'prj/group_create.html', {'form': form})

 
class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

class IndexView(TemplateView):
    template_name = 'prj/index.html'

class chat_view(TemplateView):
    template_name = 'prj/chat.html'





# Create your views here.
