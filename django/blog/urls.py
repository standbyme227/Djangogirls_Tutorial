from django.urls import path, re_path
from . import views

# from blog import views 위와 같음 왜냐하만 '.'은 현재위치를 나타내기때문에

urlpatterns = [
    path('', views.post_list),
    re_path(r'(?P<pk>\d+)/$', views.post_detail),
    # path('detail/', views.post_detail),
    # re.complie(re'(?P<pk>\d+)')
]
