from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import menuAPI, tagApi
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('menu/', menuAPI.as_view() , name='menuList'),
    path('tag/', tagApi.as_view(), name='tag')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)