from netbox.api.viewsets import NetBoxModelViewSet

from netbox_netdis.api.serializers import OnboardingTaskSerializer
from netbox_netdis.filters import OnboardingTaskFilterSet
from netbox_netdis.models import OnboardingTask


class OnboardingTaskViewSet(NetBoxModelViewSet):
    """API Viewset."""

    queryset = OnboardingTask.objects.all()
    filterset_class = OnboardingTaskFilterSet
    serializer_class = OnboardingTaskSerializer
