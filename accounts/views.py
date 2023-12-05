# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

from .forms import *
from chatapp.models import User
 
# class SignUpView(generic.CreateView):
#     form_class = RegistrationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
#
#     def save(self):
#         user = super().save(commit=False)
#         user.is_active = True
#         user.save()




class RegistrationView(generic.CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # login(self.request, self.object)
        return response

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = request.user
            return redirect(self.get_success_url())

        return super().get(request, *args, **kwargs)



class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/'
    next_page = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())

        return super().get(request, *args, **kwargs)


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UpdateForm
    template_name = 'registration/update.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user
