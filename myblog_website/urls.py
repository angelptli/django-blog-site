from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Point to myblog app
    path('', include('myblog.urls')),

    # Django user authentication package
    path('members/', include('django.contrib.auth.urls')),
    # Point to members app
    path('members/', include('members.urls')),
]
