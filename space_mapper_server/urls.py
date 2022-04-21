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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tracks.views import show_user_code, download_fix_stats, download_reg_stats


urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('tracks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mobility_mapper_code/', show_user_code, name='show_user_code'),
    url(r'^fix_stats/', download_fix_stats, name='download_fix_stats'),
    url(r'^reg_stats/', download_reg_stats, name='download_reg_stats'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^$', show_user_code),
)
