from netbox.choices import ButtonColorChoices
from netbox.plugins import PluginMenuButton, PluginMenuItem

onboardingtask_buttons = [
    PluginMenuButton(
        link="plugins:netbox_netdis:onboardingtask_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netdis:onboardingtask_list",
        link_text="Onboarding Task",
        buttons=onboardingtask_buttons,
    ),
)
