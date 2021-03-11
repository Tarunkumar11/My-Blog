"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('accounts/login', myloginview.as_view(),name='login'),
    # path('accounts/login', Signup.as_view(),name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^login/$',auth_view.LoginView.as_view(), name="login"),
    # url(r'^password_reset/$',auth_view.PasswordResetView.as_view(template_name = "registration/password_reset_form.html"),name = "reset_password"),
    # url(r'^reset_password_sent/$',auth_view.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"),name = "password_reset_done"),
    # path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirm.html"),name = "password_reset_confirm"),
    # url(r'^reset_password_complete/$',auth_view.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"),name="password_reset_complete"),
    url(r'', include('blog.urls')),
    
]
