from django.conf import settings
from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import base, ProductListView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from django.conf.urls.static import static
from django.urls import path

# from myapp.views import HomePageView

app_name = CatalogConfig.name

urlpatterns = [path("", ProductListView.as_view(), name='product_list'),
               path("<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
               path('contacts/', contacts, name='contacts'),
               path('product/create', ProductCreateView.as_view(), name='product_create'),
               path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
               path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)