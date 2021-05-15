from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("home.urls")),
    path("", include("hashtag.urls")),
    path("", include("notification.urls")),
    path("", include("chat.urls")),
    path("", include("profile_app.urls")),
    path("", include("profile_settings.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
