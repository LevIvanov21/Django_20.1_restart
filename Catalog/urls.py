from django.conf import settings
from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import index, contacts
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [path("", index), path("contacts/", contacts)] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
