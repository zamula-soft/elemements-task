from django.urls import path

from elements.api.v1 import views

urlpatterns = [
    path('images/', views.ImagesListApi.as_view()),
    path('images/<int:pk>/', views.ImagesDetailApi.as_view())
]