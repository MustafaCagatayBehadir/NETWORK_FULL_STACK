"""Model serializers for the nautobot_device_onboarding REST API."""

from dcim.api.serializers import DeviceRoleSerializer, LocationSerializer, PlatformSerializer
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from netbox_netdis.models import OnboardingTask

from .credentials import Credentials


class OnboardingTaskSerializer(NetBoxModelSerializer):
    """Serializer for the OnboardingTask model."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_netdis-api:onboardingtask-detail")
    location = LocationSerializer()
    platform = PlatformSerializer()
    role = DeviceRoleSerializer()

    class Meta:
        model = OnboardingTask

        fields = "__all__"
        read_only_fields = ["id", "created_device", "status", "failed_reason", "message"]

    def validate(self, data):
        """Custom Validate class to remove credential fields."""
        attrs = data.copy()
        username = attrs.pop("username", "")
        password = attrs.pop("password", "")
        secret = attrs.pop("secret", "")

        self.credentials = Credentials(  # pylint: disable=attribute-defined-outside-init
            username=username,
            password=password,
            secret=secret,
        )

        return super().validate(attrs)
