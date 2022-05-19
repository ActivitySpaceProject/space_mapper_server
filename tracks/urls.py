from django.urls import include, path, re_path
from rest_framework import routers
from tracks import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'write', views.DataPointViewSet, basename='write')

urlpatterns = [
    re_path(r'^', include(router.urls))
]