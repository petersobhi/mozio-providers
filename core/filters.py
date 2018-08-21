from django.contrib.gis.geos import Point

from django_filters import FilterSet
from django_filters.filters import NumberFilter


class ServiceAreaFilter(FilterSet):
    lat = NumberFilter(help_text="Latitude of a point to get intersected polygons")
    lng = NumberFilter(help_text="Longitude of a point to get intersected polygons")

    def filter_queryset(self, queryset):
        lat = self.form.cleaned_data.get('lat', None)
        lng = self.form.cleaned_data.get('lng', None)

        if lat and lng:
            point = Point(float(lat), float(lng))
            queryset = queryset.filter(polygon__intersects=point)

        return queryset
