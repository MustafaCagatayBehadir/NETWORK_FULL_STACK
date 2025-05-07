from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class NetdisView(generic.ObjectView):
    queryset = models.Netdis.objects.all()


class NetdisListView(generic.ObjectListView):
    queryset = models.Netdis.objects.all()
    table = tables.NetdisTable


class NetdisEditView(generic.ObjectEditView):
    queryset = models.Netdis.objects.all()
    form = forms.NetdisForm


class NetdisDeleteView(generic.ObjectDeleteView):
    queryset = models.Netdis.objects.all()
