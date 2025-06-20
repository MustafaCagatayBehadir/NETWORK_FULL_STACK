"""Utility functions for Netbox Netdis plugin."""

from netbox_netdis.constants import Constants


def failure(**kwargs) -> dict[str]:
    """Return dictionary with provided kwargs and predefined "status" key set to `Failure`."""
    return dict(status=Constants.Status.FAILURE_STATUS, **kwargs)


def success(**kwargs) -> dict[str]:
    """Return dictionary with provided kwargs and predefined "status" key set to `Success`."""
    return dict(status=Constants.Status.SUCCESS_STATUS, **kwargs)
