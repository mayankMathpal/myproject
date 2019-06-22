from django.conf.urls.static import static
from django.urls import path, include

from Halanxproject import settings
from Myapp import views

urlpatterns = [
    path('ok/', views.ok )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)