from rest_framework import permissions
from models import AllowedIPs


class TracksPermission(permissions.BasePermission):
    """
    Custom permission to be used with tracks data
    """

    def has_permission(self, request, view):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_addr = x_forwarded_for.split(',')[-1].strip()
        else:
            ip_addr = request.META.get('REMOTE_ADDR')
        allowed_ip = AllowedIPs.objects.filter(IP_address=ip_addr).exists()
        allowed_group = 'data_access_group' in [group.name for group in request.user.groups.all()]
        return allowed_ip and allowed_group