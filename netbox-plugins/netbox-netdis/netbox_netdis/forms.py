from dcim.models import DeviceRole, Location
from django.forms import CharField, IntegerField, MultipleChoiceField, PasswordInput
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField

from netbox_netdis.choices import OnboardingFailChoices, OnboardingStatusChoices
from netbox_netdis.models import OnboardingTask

BLANK_CHOICE = (("", "---------"),)


class OnboardingTaskForm(NetBoxModelForm):
    """Form for device onboarding tasks."""

    ip_address = CharField(
        required=True,
        label="IP Address/FQDN",
        help_text="IP Address/DNS Name of the device to onboard, specify in a comma separated list for multiple devices.",
    )

    port = IntegerField(required=False, help_text="Port to connect to the device. Defaults to 22 for SSH.")

    timeout = IntegerField(required=False, help_text="Timeout in seconds for the connection. Defaults to 30 seconds.")

    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        query_params={"content_type": "dcim.device"},
        help_text="Select the location for the device.",
    )

    role = DynamicModelChoiceField(
        queryset=DeviceRole.objects.all(),
        help_text="Device role.",
    )

    username = CharField(required=False, help_text="Device username (will not be stored in database)")

    password = CharField(
        required=False, widget=PasswordInput, help_text="Device password (will not be stored in database)"
    )

    secret = CharField(required=False, widget=PasswordInput, help_text="Device secret (will not be stored in database)")

    class Meta:
        model = OnboardingTask
        fields = [
            "location",
            "ip_address",
            "port",
            "timeout",
            "username",
            "password",
            "secret",
            "role",
        ]


class OnboardingTaskFilterForm(NetBoxModelForm):
    """Form for filtering OnboardingTask instances."""

    location = DynamicModelChoiceField(
        queryset=Location.objects.all(), query_params={"content_type": "dcim.device"}, required=False
    )

    status = MultipleChoiceField(
        choices=BLANK_CHOICE + OnboardingStatusChoices.CHOICES,
        required=False,
    )

    failed_reason = MultipleChoiceField(
        choices=BLANK_CHOICE + OnboardingFailChoices.CHOICES,
        required=False,
        label="Failed Reason",
    )

    q = CharField(required=False, label="Search")

    class Meta:
        model = OnboardingTask
        fields = ["q", "location", "status", "failed_reason"]
