from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import ServiceAreaFilter

User = get_user_model()


class ServiceAreaListView(ListCreateAPIView):
    """
    get:
    Return a list of all the existing service areas.

    post:
    Create a new service area.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ServiceAreaFilter

    def create(self, request, *args, **kwargs):
        serializer = ServiceAreaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(provider=request.user.provider)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ServiceAreaDetailsView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a service area object using the id.

    put:
    Modify a service area object (Owner provider must be authenticated)

    delete:
    Delete a service area object (Owner provider must be authenticated)
    """
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ProviderListView(ListAPIView):
    """
    get:
    Return a list of all the existing providers.
    """
    queryset = User.objects.all()
    serializer_class = ProviderSerializer
