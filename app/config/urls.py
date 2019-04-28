from django.conf import settings
from django.contrib import admin
from django.urls import path, include


admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_INDEX_TITLE


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('shop.urls')),
    path('', include('contacts.urls')),
    path('blog/', include('blog.urls')),
    path('mailmagazine/', include('mailmagazine.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('search/', include('search.urls')),
    path(settings.ADMIN_URL + '/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
