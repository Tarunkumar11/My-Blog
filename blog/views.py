from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.http import HttpResponse
from . import forms
from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from blog.forms import PostForm,CommentForm,SignupForm,QueryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView,
                                    RedirectView)
from blog.models import Blog_post,Blog_comments
# Create your views here.


class HomeView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['blogs'] = Blog_post.objects.all()[:6]
        context['i'] = 0
        return context




class Signup(CreateView):
    form_class = forms.SignupForm
    success_url = reverse_lazy("login")
    template_name = "blog/user_signup.html"

def AddQueryForm(request):
    if request.method == "POST":
        form = QueryForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Invalids details")
    else:
        form = QueryForm()
    return render(request,'blog/user_contact.html',{'form':form})





class AboutView(TemplateView):
    template_name = 'blog/about.html'




# class PostListView(ListView):
#     template_name = 'blog/home'
#     model = Post
#     def get_queryset(self):
#         return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date')

class PostDetailView(DetailView):
    model = Blog_post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url  = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Blog_post
    fields = ("title","text")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url  = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Blog_post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog_post
    success_url = reverse_lazy('home')

class DraftListView(LoginRequiredMixin,ListView):
    val = None
    login_url = '/login/'
    redirect_field_name = 'blog/home.html'
    model = Blog_post
    def get(self, request, *args, **kwargs):
        global val
        val = request.user.id
        return super(LoginRequiredMixin, self).get(request, *args, **kwargs)
    
    def get_queryset(self):
        global val
        return Post.objects.filter(Q(publish_date__isnull = True) & Q(author_id=val)).order_by('-create_date')

class LogOutView(RedirectView):
    url = reverse_lazy('home')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Blog_post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment(request,pk):
    post = get_object_or_404(Blog_post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.author = request.user.username
        if form.is_valid():
            form.cleaned_data['author'] = request.user.first_name
            comment = form.save(commit = False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            return redirect('post_detail',pk = post.pk)
        else:
            return HttpResponse("Invalid Entery")
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Blog_comments, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
