from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),
]