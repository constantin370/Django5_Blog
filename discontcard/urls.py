from django.urls import path

from discontcard.views import DiscontManagerView

app_name = "discontcard"

urlpatterns = [
    path('', DiscontManagerView.as_view(), name='discontcard'),
]
