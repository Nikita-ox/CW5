from rest_framework.viewsets import ModelViewSet
from ads.views.ads import Location
from ads.views.ads import LocationSerializer


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
