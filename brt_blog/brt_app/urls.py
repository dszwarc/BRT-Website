from django.urls import path
from .views import AddPostView, HomeView, ArticleDetailView

urlpatterns = [
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('', HomeView.as_view(), name='home'),
]
