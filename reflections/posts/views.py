from django.shortcuts import render, get_object_or_404

from .models import Post, Group

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    groups = Group.objects.all()
    context = {
        'posts': posts,
        'groups': groups,
    }
    return render(request, template, context)

def posts_page(request, slug):
    template = 'posts/posts_page.html'
    group = get_object_or_404(Group, slug=slug)
    groups = Group.objects.all()
    posts = group.posts.all()
    context = {
        'posts': posts,
        'group': group,
        'groups': groups,
    }
    return render(request, template, context)