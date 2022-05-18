"""space_mapper_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin, auth
from tracks.views import show_user_code, show_landing_page, download_fix_stats, download_reg_stats


urlpatterns = [
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/', include('tracks.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^mobility_mapper_code/', show_user_code, name='show_user_code'),
    re_path(r'^fix_stats/', download_fix_stats, name='download_fix_stats'),
    re_path(r'^reg_stats/', download_reg_stats, name='download_reg_stats'),
    re_path(r'^accounts/login/$', auth.views.LoginView.as_view(), name='auth_login'),
    re_path(r'^$', show_landing_page)
]
