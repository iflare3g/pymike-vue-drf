from django.urls import path
from .views import ArticleListViewAPIView, ArticleDraftListAPIView, ArticleDetailAPIView

urlpatterns = [
    path("articles/", ArticleListViewAPIView.as_view(), name="article-list"),
    path(
        "articles/drafts/",
        ArticleDraftListAPIView.as_view(),
        name="article-drafted-list",
    ),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
]
