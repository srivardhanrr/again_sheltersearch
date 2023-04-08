from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('dashboard/', include(('main.urls', 'main'), namespace='main')),

    path('i18n/', include('django.conf.urls.i18n')),

    path('accounts/', include('accounts.urls')),
    path('allaccounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
