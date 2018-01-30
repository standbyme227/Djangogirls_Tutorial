from django.shortcuts import  render


def post_list(request):
    return render(request, 'blog/post_list.html')
    #return HttpResponse('<html><body><h1>Post list</h1><p>Post목록을 보여줄 예정입니다.</p></body>')
