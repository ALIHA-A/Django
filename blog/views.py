from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts= Post.objects.filter(published_date__lte= timezone.now())
    posts= Post.objects.order_by("-published_date")
    context= {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    # post= get_object_or_404(Post, pk= pid, status= 1)
    # context= {'post':post}
    post= Post.objects.filter(published_date__lte= timezone.now())
    post= Post.objects.order_by('-published_date')
    return render(request,"blog/blog-single.html", {'posts':post})

# def blog_test(request, pid):
#     # post= Post.objects.get(id= pid)
#     post= get_object_or_404(Post, pk= pid)
#     context= {'post':post}
#     return render(request, 'test.html', context) 
