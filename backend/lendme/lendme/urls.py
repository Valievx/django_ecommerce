from django.contrib import admin
from django.urls import include, path

from lendme.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('catalog.urls', namespace='catalog'))
]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
