from django.shortcuts import render, get_object_or_404
from .models import Post, Kategori, Tag

def home(request):
    posts = Post.objects.all().order_by('-tanggal_publikasi')
    return render(request, 'myblog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'myblog/post_detail.html', {'post': post})

def kategori_detail(request, slug):
    kategori = get_object_or_404(Kategori, slug=slug)
    posts = kategori.posts.all().order_by('-tanggal_publikasi')
    return render(request, 'myblog/kategori_detail.html', {'kategori': kategori, 'posts': posts})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.all().order_by('-tanggal_publikasi')
    return render(request, 'myblog/tag_detail.html', {'tag': tag, 'posts': posts})