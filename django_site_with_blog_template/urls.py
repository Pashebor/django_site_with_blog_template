from django.contrib import admin
from django .urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('app_business_card.urls')),
    path('blog/', include('app_business_card_blog.urls'))
] + static(settings.STATIC_URL, document_root=settings.MEDIA_URL)
