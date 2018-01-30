from django.http import HttpResponse


def post_list(request):
    return HttpResponse('<html><body><h1>Post list</h1><p>Post목록을 보여줄 예정입니다.</p></body>')
