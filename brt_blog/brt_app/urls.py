from django.urls import path
from .views import DeletePostView, AddPostView, HomeView, ArticleDetailView, UpdatePostView

urlpatterns = [
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('', HomeView.as_view(), name='home'),
]
