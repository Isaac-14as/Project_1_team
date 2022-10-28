from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts_page/<slug:slug>/', views.posts_page, name='posts_page'),
    # path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
