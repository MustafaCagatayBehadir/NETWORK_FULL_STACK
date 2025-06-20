from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from netbox.views.generic import BulkDeleteView, ObjectDeleteView, ObjectEditView, ObjectListView, ObjectView

from netbox_netdis.filters import OnboardingTaskFilterSet
from netbox_netdis.forms import OnboardingTaskFilterForm, OnboardingTaskForm
from netbox_netdis.models import OnboardingTask
from netbox_netdis.tables import OnboardingTaskTable


class OnboardingTaskView(ObjectView):
    queryset = OnboardingTask.objects.all()


class OnboardingTaskListView(ObjectListView):
    queryset = OnboardingTask.objects.all()
    table = OnboardingTaskTable
    filterset = OnboardingTaskFilterSet
    filterset_form = OnboardingTaskFilterForm


class OnboardingTaskEditView(ObjectEditView):
    queryset = OnboardingTask.objects.all()
    form = OnboardingTaskForm


class OnboardingTaskDeleteView(ObjectDeleteView):
    queryset = OnboardingTask.objects.all()


class OnboardingTaskBulkDeleteView(BulkDeleteView):
    queryset = OnboardingTask.objects.all()
    filterset = OnboardingTaskFilterSet
    table = OnboardingTaskTable


def onboardingtask_sync(request, pk):
    task = get_object_or_404(OnboardingTask, pk=pk)
    task.sync()
    messages.success(request, f"Sync started for OnboardingTask {task.pk}")
    return redirect(task.get_absolute_url())
