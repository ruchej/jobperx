from django.urls import path
from . import views
from . import api


urlpatterns = [
    path("api/upload/", api.UploadFile.as_view(), name="upload"),
    path("api/status/<int:pk>", api.GetStatus.as_view(), name="status"),
]
