from django.urls import path, re_path
from . import views

# from blog import views 위와 같음 왜냐하만 '.'은 현재위치를 나타내기때문에

urlpatterns = [
    path('', views.post_list, name='post-list'),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('<int:pk>/', views.post_detail, name='post-detail'),

    path('<int:pk>/edit/', views.post_edit, name='post-edit'),


    path('add/', views.post_add, name='post-add'),

    path('<int:pk>/delete/', views.post_delete, name='post-delete'),
    # path('detail/', views.post_detail),
    # re.complie(re'(?P<pk>\d+)')
]
