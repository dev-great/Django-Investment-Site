from django.contrib import admin
from django.urls import path, include
from accounts import views
from core import views
from contact import views
from pages import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('pages/', include('pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header ="Future Trade Option control panel"
admin.site.index_title ="Administrators dashboard"
admin.site.site_title ="Control panel"
