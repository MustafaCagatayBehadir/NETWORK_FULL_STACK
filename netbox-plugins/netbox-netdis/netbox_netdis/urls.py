"""Django urlpatterns declaration for netbox_netdis plugin."""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from netbox_netdis import views
from netbox_netdis.models import OnboardingTask

urlpatterns = [
    path(
        "onboardingtasks/",
        views.OnboardingTaskListView.as_view(),
        name="onboardingtask_list",
    ),
    path(
        "onboardingtasks/add/",
        views.OnboardingTaskEditView.as_view(),
        name="onboardingtask_add",
    ),
    path(
        "onboardingtask/<int:pk>/",
        views.OnboardingTaskView.as_view(),
        name="onboardingtask",
    ),
    path(
        "onboardingtask/<int:pk>/edit/",
        views.OnboardingTaskEditView.as_view(),
        name="onboardingtask_edit",
    ),
    path(
        "onboardingtask/<int:pk>/delete/",
        views.OnboardingTaskDeleteView.as_view(),
        name="onboardingtask_delete",
    ),
    path(
        "onboardingtask/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="onboardingtask_changelog",
        kwargs={"model": OnboardingTask},
    ),
    path("onboardingtask/<int:pk>/sync/", views.onboardingtask_sync, name="onboardingtask_sync"),
]
