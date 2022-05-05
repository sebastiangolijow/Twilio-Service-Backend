from django.urls import path
from src.service.smschecker.views import HelloTwillio

app_name = "smschecker"

urlpatterns = [
    path("smschecker", HelloTwillio.as_view(), name="helloword"),
    path("smschecker", HelloTwillio.as_view(), name="smschecker"),
]
