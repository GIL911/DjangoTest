from django.urls import path, re_path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    #write
    path('write/', views.write, name='write'),
    #List
    path('List/', views.list, name='list'),
    path('vue/', views.vue, name='vue'),
    path('vue1/', views.vue1, name='vue1'),
    # view
    #re_path(r'^post(.*)/$', blog_views.post),
    #re_path(r'^view/([0-9])/$', views.view, name='view')
    re_path(r'^view/(?P<num>[0-9]+)/$', views.view, name='view')
]