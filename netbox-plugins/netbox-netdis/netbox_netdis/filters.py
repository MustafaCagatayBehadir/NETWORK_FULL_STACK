import django_filters
from dcim.models import DeviceRole, Location
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from utilities.forms.fields import DynamicModelChoiceField

from netbox_netdis.models import OnboardingTask


class OnboardingTaskFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for OnboardingTask instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        label="Location (name)",
    )

    role = django_filters.ModelMultipleChoiceFilter(
        queryset=DeviceRole.objects.all(),
        label="Device Role (name)",
    )

    class Meta:
        model = OnboardingTask
        fields = ["id", "location", "role", "status", "failed_reason"]

    def search(self, queryset, name, value):  # pylint: disable=unused-argument
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(id__icontains=value)
            | Q(ip_address__icontains=value)
            | Q(location__name__icontains=value)
            | Q(created_device__name__icontains=value)
            | Q(status__icontains=value)
            | Q(failed_reason__icontains=value)
            | Q(message__icontains=value)
        )
        return queryset.filter(qs_filter)
