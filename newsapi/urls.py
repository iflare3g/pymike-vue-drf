from django.urls import path
from .views import article_list, article_drafted_list

urlpatterns = [
    path("articles/", article_list, name="article-list"),
    path("articles/drafts/", article_drafted_list, name="article-drafted-list"),
]
