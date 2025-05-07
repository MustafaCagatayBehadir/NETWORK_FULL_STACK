from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("netdiss/", views.NetdisListView.as_view(), name="netdis_list"),
    path("netdiss/add/", views.NetdisEditView.as_view(), name="netdis_add"),
    path("netdiss/<int:pk>/", views.NetdisView.as_view(), name="netdis"),
    path("netdiss/<int:pk>/edit/", views.NetdisEditView.as_view(), name="netdis_edit"),
    path("netdiss/<int:pk>/delete/", views.NetdisDeleteView.as_view(), name="netdis_delete"),
    path(
        "netdiss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="netdis_changelog",
        kwargs={"model": models.Netdis},
    ),
)
