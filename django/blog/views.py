from django.shortcuts import render
from .models import Post


def post_list(request):

    posts = Post.objects.all()
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
