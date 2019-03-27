from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("prodotto/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
