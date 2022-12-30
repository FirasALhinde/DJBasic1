from django.shortcuts import render,get_object_or_404
from.models import Post
# Create your views here.

def post_list(request):
    all_posts = Post.objects.all()
    context = {'all_posts':all_posts}
    return render(request,'blog/post_list.html',context)

def post_detail(request,id):
    post = get_object_or_404 (Post,id=id)
    return render(request,'blog/post_detail.html',{'post':post})