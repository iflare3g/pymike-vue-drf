from django.urls import path
from .views import article_list, article_drafted_list, article_detail_view

urlpatterns = [
    path("articles/", article_list, name="article-list"),
    path("articles/drafts/", article_drafted_list, name="article-drafted-list"),
    path("articles/<int:pk>/", article_detail_view, name="article-detail"),
]
