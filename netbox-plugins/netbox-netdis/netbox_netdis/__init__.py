"""Top-level package for Netbox Netdis."""

__author__ = """Mustafa Behadir"""
__email__ = "mustafabehadir@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class NetdisConfig(PluginConfig):
    name = "netbox_netdis"
    verbose_name = "Netbox Netdis"
    description = "Network Hardware Discovery Plugin"
    author = "Mustafa Behadir"
    author_email = "mustafabehadir@gmail.com"
    version = "0.1.0"
    base_url = "netbox_netdis"


config = NetdisConfig
