from netbox.filtersets import NetBoxModelFilterSet
from .models import Netdis


# class NetdisFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = Netdis
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
