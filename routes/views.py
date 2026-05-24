from rest_framework import viewsets

from .models import Route
from .serializers import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.order_by("id")
    serializer_class = RouteSerializer
