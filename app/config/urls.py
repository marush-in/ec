from django.conf import settings
from django.contrib import admin
from django.urls import path, include


admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_INDEX_TITLE


urlpatterns = [
    path('', include('shop.urls')),
    path('', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
