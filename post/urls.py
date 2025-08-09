from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView)

urlpatterns = [
    path('',PostListView.as_view(), name="post_list"),
    path('<int:pk>/',PostDetailView.as_view(), name="post_detail"),#--this will retrieve a single element form the db, the primary key (pk) is an integer(int)--
    path('new/', PostCreateView.as_view(), name="post_new")
]