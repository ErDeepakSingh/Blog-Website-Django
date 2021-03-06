from django.conf.urls import url,include
from django.contrib import admin
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("blog.urls")),
# http://127.0.0.1:8000/users
    url(r'^users/', include("users.urls")),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
