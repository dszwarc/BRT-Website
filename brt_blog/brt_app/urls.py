from django.urls import path
from .views import HomeView, ArticleDetailView

urlpatterns = [
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('', HomeView.as_view(), name='home'),
]
