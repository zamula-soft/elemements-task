from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from elements import views

schema_view = get_swagger_view(title='Elements ImageData API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', views.ImageDataList.as_view()),
    path('images/<int:pk>', views.ImageDataDetailView.as_view()),
    path('api/', include('elements.api.urls')),
    path('openapi/', schema_view),

]

urlpatterns = format_suffix_patterns(urlpatterns)
