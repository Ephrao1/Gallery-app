from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from photos import views

urlpatterns=[
    url('^$', views.index, name='index'),
    url(r'^search/', views.search_photo, name='search_photo'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)', views.single_image, name='single_image'),
    url(r'^location/(?P<image_location>\d+)', views.location, name='location'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
