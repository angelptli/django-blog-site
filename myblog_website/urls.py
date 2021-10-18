from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Point to myblog app
    path('', include('myblog.urls')),

    # Django user authentication package
    path('members/', include('django.contrib.auth.urls')),

    # Point to members app
    path('members/', include('members.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
