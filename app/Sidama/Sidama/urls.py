"""sidama URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from SidamaApp.views import SidamaViewSet, UserViewSet, \
    RoasterViewSet, CountryViewSet, RegionViewSet,\
    VarietalViewSet, QualityViewSet, BeanViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'sidama', SidamaViewSet)
router.register(r'roasters', RoasterViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'varietals', VarietalViewSet)
router.register(r'qualities', QualityViewSet)
router.register(r'beans', BeanViewSet)
router.register(r'tags', TagViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [url(r'^api/', include(router.urls)), ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns.append(url(r'^api/', include('rest_framework.urls',
                                             namespace='rest_framework')))
    urlpatterns.append(url(r'^admin/', admin.site.urls))
