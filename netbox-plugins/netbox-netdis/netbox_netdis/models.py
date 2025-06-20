from core.choices import JobIntervalChoices
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel, RestrictedQuerySet

from netbox_netdis.choices import OnboardingFailChoices, OnboardingStatusChoices
from netbox_netdis.exceptions import NaaSServiceException
from netbox_netdis.jobs import OnboardingJob
from netbox_netdis.utils import failure


class OnboardingTask(NetBoxModel):
    """The status of each onboarding Task is tracked in the OnboardingTask table."""

    label = models.PositiveIntegerField(default=0, editable=False, help_text="Label for sorting tasks")

    created_device = models.ForeignKey(to="dcim.Device", on_delete=models.SET_NULL, blank=True, null=True)

    ip_address = models.CharField(
        max_length=255,
        help_text="primary ip address for the device",
    )

    location = models.ForeignKey(to="dcim.Location", on_delete=models.SET_NULL, blank=True, null=True)

    role = models.ForeignKey(
        to="dcim.DeviceRole",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    platform = models.ForeignKey(to="dcim.Platform", on_delete=models.SET_NULL, blank=True, null=True)

    status = models.CharField(
        max_length=255, choices=OnboardingStatusChoices, help_text="Overall status of the task", blank=True, default=""
    )

    failed_reason = models.CharField(
        max_length=255,
        choices=OnboardingFailChoices,
        help_text="Reason why the task failed (optional)",
        blank=True,
        default="",
    )

    message = models.CharField(max_length=511, blank=True)

    port = models.PositiveSmallIntegerField(help_text="Port to use to connect to the device", default=22)

    timeout = models.PositiveSmallIntegerField(
        help_text="Timeout period in seconds to wait while connecting to the device", default=30
    )

    def __str__(self):
        """String representation of an OnboardingTask."""
        return f"{self.location} | {self.ip_address}"

    def get_absolute_url(self):  # pylint: disable=arguments-differ
        """Provide absolute URL to an OnboardingTask."""
        return reverse("plugins:netbox_netdis:onboardingtask", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        """Overwrite method to get latest label value and update Task object."""
        if not self.label:
            latest_task = OnboardingTask.objects.all().order_by("-label").first()
            self.label = (latest_task.label if latest_task else 0) + 1
        OnboardingJob.enqueue_once(kwargs={"task_id": self.pk}, interval=JobIntervalChoices.INTERVAL_HOURLY)
        return super().save(*args, **kwargs)

    def sync(self):
        OnboardingJob.enqueue(instance=self)

    objects = RestrictedQuerySet.as_manager()

    class Meta:
        """Class Meta."""

        unique_together = ("label", "ip_address")
        ordering = ("label",)
        app_label = "netbox_netdis"


class OnboardingDevice(NetBoxModel):
    """The status of each Onboarded Device is tracked in the OnboardingDevice table."""

    device = models.OneToOneField(to="dcim.Device", on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True, help_text="Whether (re)onboarding of this device is permitted")

    @property
    def last_check_attempt_date(self):
        """Date of last onboarding attempt for a device."""
        if self.device.primary_ip4:
            try:
                return (
                    OnboardingTask.objects.filter(
                        ip_address=self.device.primary_ip4.address.ip.format()  # pylint: disable=no-member
                    )
                    .latest("last_updated")
                    .created
                )
            except OnboardingTask.DoesNotExist as err:
                raise NaaSServiceException(failure(message="No onboarding task found for this device.")) from err
        else:
            return NaaSServiceException(failure(message="No primary IP address found for this device."))

    @property
    def last_check_successful_date(self):
        """Date of last successful onboarding for a device."""
        if self.device.primary_ip4:
            try:
                return (
                    OnboardingTask.objects.filter(
                        ip_address=self.device.primary_ip4.address.ip.format(),  # pylint: disable=no-member
                        status=OnboardingStatusChoices.STATUS_SUCCEEDED,
                    )
                    .latest("last_updated")
                    .created
                )
            except OnboardingTask.DoesNotExist as err:
                raise NaaSServiceException(failure(message="No onboarding task found for this device.")) from err
        else:
            return NaaSServiceException(failure(message="No primary IP address found for this device."))

    @property
    def status(self):
        """Last onboarding status."""
        if self.device.primary_ip4:
            try:
                return (
                    OnboardingTask.objects.filter(
                        ip_address=self.device.primary_ip4.address.ip.format()  # pylint: disable=no-member
                    )
                    .latest("last_updated")
                    .status
                )
            except OnboardingTask.DoesNotExist as err:
                raise NaaSServiceException(failure(message="No onboarding task found for this device.")) from err
        else:
            raise NaaSServiceException(failure(message="No primary IP address found for this device."))

    @property
    def last_ot(self):
        """Last onboarding task."""
        if self.device.primary_ip4:
            try:
                return OnboardingTask.objects.filter(
                    ip_address=self.device.primary_ip4.address.ip.format()  # pylint: disable=no-member
                ).latest("last_updated")
            except OnboardingTask.DoesNotExist as err:
                raise NaaSServiceException(failure(message="No onboarding task found for this device.")) from err
        else:
            raise NaaSServiceException(failure(message="No primary IP address found for this device."))
