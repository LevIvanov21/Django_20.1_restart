from django.conf import settings
from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import  product_list
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [path("", product_list, name='product_list')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
