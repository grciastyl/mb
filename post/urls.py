from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)

urlpatterns = [
    path('',PostListView.as_view(), name="post_list"),
    path('<int:pk>/',PostDetailView.as_view(), name="post_detail"),#--this will retrieve a single element form the db, the primary key (pk) is an integer(int)--
    path('new/', PostCreateView.as_view(), name="post_new"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name= "post_edit"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name= "post_delete"),
]