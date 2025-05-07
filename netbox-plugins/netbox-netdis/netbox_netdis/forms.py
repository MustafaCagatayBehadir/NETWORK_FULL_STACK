from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import Netdis


class NetdisForm(NetBoxModelForm):
    class Meta:
        model = Netdis
        fields = ("name", "tags")
