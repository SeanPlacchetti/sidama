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
router.register(r'roaster', RoasterViewSet)
router.register(r'country', CountryViewSet)
router.register(r'region', RegionViewSet)
router.register(r'varietal', VarietalViewSet)
router.register(r'quality', QualityViewSet)
router.register(r'bean', BeanViewSet)
router.register(r'tag', TagViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [url(r'^api/', include(router.urls)), ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns.append(url(r'^api/', include('rest_framework.urls',
                                             namespace='rest_framework')))
    urlpatterns.append(url(r'^admin/', admin.site.urls))
