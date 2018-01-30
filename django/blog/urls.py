from django.urls import path
from . import views

# from blog import views 위와 같음 왜냐하만 '.'은 현재위치를 나타내기때문에

urlpatterns = [
    path('', views.post_list),
    path('detail/', views.post_detail),
]
