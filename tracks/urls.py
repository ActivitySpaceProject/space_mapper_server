from django.urls import include, path
from rest_framework import routers
from tracks import views


router = routers.DefaultRouter()
router.register(r'data_points', views.DataPointViewSet)
router.register(r'read_data_points', views.ReadDataPointViewSet)


urlpatterns = ['tracks.views',
    path('^', include(router.urls)),
]