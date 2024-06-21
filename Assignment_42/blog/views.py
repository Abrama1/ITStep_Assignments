from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "blog/index.html"
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        posts = Post.objects.all()
        return render(request, self.template_name, {"posts": posts})


class MyPostsView(PermissionRequiredMixin, TemplateView):
    template_name = "blog/myposts.html"
    permission_required = "blog.add_post"
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        myposts = Post.objects.filter(author = request.user)
        return render(request, self.template_name, {"myposts": myposts})


class PostDetailView(PermissionRequiredMixin, DetailView):
    
    model = Post
    template_name = "blog/post_info.html"
    context_object_name = "post_info"
    login_url = "/login"
    permission_required = "blog.view_post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        previous_url = self.request.META.get('HTTP_REFERER')
        context['go_back_url'] = previous_url if previous_url else reverse('index')
        return context


class AddPostView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    success_url = reverse_lazy("myposts")
    permission_required = "blog.add_post"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        post = form.save(commit=False)
        post.author = self.request.user
        form.save()
        return super().form_valid(form)


class EditPostView(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/edit_post.html"
    permission_required = "blog.change_post"
    success_url = reverse_lazy("myposts")


class DeletePostView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    permission_required = "blog.delete_post"
    
    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy("index")
        return reverse_lazy("myposts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        previous_url = self.request.META.get('HTTP_REFERER')
        context['go_back_url'] = previous_url if previous_url else reverse('index')
        return context
    
