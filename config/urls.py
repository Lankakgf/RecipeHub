from django.http import HttpResponse

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('service-worker.js', lambda r: HttpResponse('', content_type='application/javascript')),

    path('admin/', admin.site.urls),
path('accounts/', include('django.contrib.auth.urls')),
path('orders/', include('orders.urls')),
    path('', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
