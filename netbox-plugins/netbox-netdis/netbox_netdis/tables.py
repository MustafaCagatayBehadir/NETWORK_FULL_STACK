import django_tables2 as tables
from netbox.tables import NetBoxTable, ToggleColumn

from netbox_netdis.models import OnboardingTask


class OnboardingTaskTable(NetBoxTable):
    """Table for displaying OnboardingTask instances."""

    pk = ToggleColumn()
    label = tables.LinkColumn()
    location = tables.LinkColumn()
    created_device = tables.LinkColumn()

    class Meta(NetBoxTable.Meta):
        model = OnboardingTask
        fields = (
            "pk",
            "label",
            "created",
            "ip_address",
            "location",
            "created_device",
            "status",
            "failed_reason",
            "message",
        )
