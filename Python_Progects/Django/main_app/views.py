from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EmailPostForm, RegisterUser,AutentUser, ContactForm, CommentForm
from django.views.generic import ListView, CreateView, FormView
from .utils import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
#def index(request):
#    news = Articles.objects.all()
#    return render(request, 'main_app/index.html', {'news':news})

class Paper_News(DataMixin, ListView):
    paginate_by = 2
    model = Articles
    template_name = 'main_app/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))

        return context

def forms(request):
    bod = Articles.objects.all()
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index.html')
            except:
                form.add_error(None, 'Error adding post')
    else:
        form = EmailPostForm()
        return render(request, 'main_app/body.html',{'bod': bod, 'form':form})

def post_news(request, post_id):
    post = get_object_or_404(Articles, pk = post_id)
    context = Articles.objects.all()
    return render(request,'main_app/main_txt.html', {'context':context, 'post':post})

class RegisterUsers(DataMixin,CreateView):
    form_class = RegisterUser
    template_name = 'main_app/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))

        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main_app/aut.html'

    def get_context_data(self, *,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_us(request):
    logout(request)
    return redirect('aut')

class Captcha(DataMixin, CreateView):
    form_class = ContactForm
    template_name = 'main_app/captcha'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Authorization')


