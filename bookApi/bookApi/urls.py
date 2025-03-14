from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from post_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('useraccount.urls')),
    path('book/', include('post_api.urls')),
    path("", views.home)
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
