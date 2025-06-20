from netbox.api.routers import NetBoxRouter

from . import views

app_name = "netbox_netdis"

router = NetBoxRouter()
router.register("onboardingtask", views.OnboardingTaskViewSet, basename="onboardingtask")
urlpatterns = router.urls
