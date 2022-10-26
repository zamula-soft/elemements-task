from django.urls import path, include

urlpatterns = [
    path('v1/', include('elements.api.v1.urls')),
]