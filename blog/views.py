from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView, 
DetailView, 
CreateView
)


posts = Post.objects.all()


def home(request):
    my_context = {
        "posts": posts
    }
    return render(request, "blog/home.html", my_context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = "/"
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def about(request):
    return render(request, "blog/about.html")