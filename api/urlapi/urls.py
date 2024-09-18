from django.urls import path
from .views import URLStreamView

urlpatterns = [
    path('stream-urls/', URLStreamView.as_view(), name='stream_urls'),
]
