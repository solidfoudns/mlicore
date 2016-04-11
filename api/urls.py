from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, url, include
from api.views import (
    OrdenViewSet, PingView
)

orden_list = OrdenViewSet.as_view({
    'get': 'list'
})

router = DefaultRouter()
router.register(r'orden', OrdenViewSet)


urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'ping/$', PingView.as_view(), name='ping'),
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

)