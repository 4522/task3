# from django.urls import path
from . import views
from django.conf.urls import url

# urlpatterns = [
#             path('', views.post_list, name='post_list'),
#             path('post/<int:pk>/', views.post_detail, name='post_detail'),
#             path('post/new/', views.post_new, name='post_new'),
#             ]
urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit'),
]