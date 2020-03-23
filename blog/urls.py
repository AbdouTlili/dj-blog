from django.urls import path 
from .views import BlogListView, BlogDetailView, BlogCreateView,BlogPostUpdateView,BlogPostDeleteView

urlpatterns = [
    path('',BlogListView.as_view(),name='home'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/',BlogPostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',BlogPostDeleteView.as_view(),name='post_delete'),
]
