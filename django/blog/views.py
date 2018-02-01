from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):

    posts = Post.objects.all() #.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # return HttpResponse('<html><body><h1>Post list</h1><p>Post목록을 보여줄 예정입니다.</p></body>')


def post_detail(request, pk):
    context= {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content

        post.save()
        return redirect('post-detail', pk=post.pk)

    post = Post.objects.get(pk=pk)
    context={
      'post': post
    }

    return render(request, 'blog/post_add_edit.html', context)

def post_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content
        )
        return redirect('post-detail', pk=post.pk)
    else:
        return render(request, 'blog/post_add_edit.html')


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if request.user == post.author:
            post.delete()
            return redirect('post-list')
        return redirect('post-detail', pk=post.pk)

