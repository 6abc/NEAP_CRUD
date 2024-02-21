from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secret/', admin.site.urls),
    path('', include('app1.urls')),
    path('captcha/', include('captcha.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Movie Login"
admin.site.site_title = "Movie Database"
admin.site.index_title = "Movie Login"
