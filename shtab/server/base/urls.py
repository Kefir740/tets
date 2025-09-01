from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
]

if DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()
