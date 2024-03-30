from django.utils import timezone
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'archive/post_list.html', {'posts': posts})


def error_404_view(request, exception):
    data = {}
    return render(request, 'archive/404.html', data)
