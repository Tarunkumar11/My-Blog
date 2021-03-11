from django.shortcuts import render
from users.admin import MyUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# class Signup(CreateView):
#     #form_class =  MyUserCreationForm
#     success_url = reverse_lazy("login")
#     # template_name = "blog/login.html"
#     # def get_context_data(self, **kwargs):
#     #     context = super(self.__class__, self).get_context_data(**kwargs)
#     #     context['signupform'] =  MyUserCreationForm()
#     #     print('**&&&&&&&&**********',context)
#     #     return context

# class myloginview(Signup,LoginView):
    
#     def get_context_data(self, **kwargs):
#         context = super(myloginview, self).get_context_data(**kwargs)
#         context['form2'] = MyUserCreationForm()
#         print('context****',context)
#         return context

   
    
    