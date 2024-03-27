from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.urls import reverse_lazy


# Create your views here.

class indexView(TemplateView):
    template_name = "index.html"

class chatView(ListView):
    template_name = "chat.html"
    model = chatTable

class chatSayView(CreateView):
    template_name = "chat_say.html"
    form_class = chatForm
    success_url = reverse_lazy("myapp:chat")

class loginView(TemplateView):
    template_name = "login.html"
    
    success_url = reverse_lazy("myapp:index")
    
class loginSuccessView(TemplateView):
    template_name = "login_success.html"

class registerView(CreateView):
    template_name = "register.html"
    form_class = userForm
    success_url = reverse_lazy("myapp:index")
