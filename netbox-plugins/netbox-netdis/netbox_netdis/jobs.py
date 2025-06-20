"""Device Onboarding Jobs."""

from netbox.jobs import JobRunner

from netbox_netdis.logger import logger


class OnboardingJob(JobRunner):
    """Netbox Job for onboarding a new device (original)."""

    class Meta:
        name = "Device Onboarding Task"

    def run(self, *args, **kwargs):
        obj = self.job.object
        logger.info(f"Running onboarding task for {obj.name} ({obj.pk})")
