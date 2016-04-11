from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import  reverse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.
from .mixins import JSONResponseMixin
from ecomerce.orders.models import Orden
from .serializers import OrdenSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'orden': reverse('orden-list', request=request, format=format),
    })

class PingView(APIView):
    def get(self, request):
        data = {'ping':'ping'}
        return JSONResponseMixin(data)

class OrdenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =Orden.objects.all()
    serializer_class = OrdenSerializer
    permission_classes = ( permissions.IsAuthenticatedOrReadOnly,)



