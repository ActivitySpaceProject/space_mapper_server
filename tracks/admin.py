from django.contrib import admin
from tracks.models import *


class DataPointAdmin(admin.ModelAdmin):
    list_display = ('user_UUID', 'user_code',  'app_version', 'type_of_data', 'last_modified', 'created',)
    readonly_fields = ('user_UUID', 'user_code', 'os', 'app_version','type_of_data', 'encrypted_message', 'encrypted_lon', 'encrypted_lat', 'encrypted_unix_time', 'encrypted_speed', 'encrypted_altitude', 'encrypted_activity', 'message', 'lon', 'lat', 'unix_time', 'speed', 'altitude', 'activity', 'last_modified', 'created',)
    fields = ('user_UUID', 'user_code', 'os', 'app_version', 'type_of_data', 'encrypted_message', 'encrypted_lon', 'encrypted_lat', 'encrypted_unix_time', 'encrypted_speed', 'encrypted_altitude', 'encrypted_activity', 'message', 'lon', 'lat', 'unix_time', 'speed', 'altitude', 'activity', 'last_modified', 'created',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AllowedIPsAdmin(admin.ModelAdmin):
    list_display = ('IP_address', 'name',)
    fields = ('IP_address', 'name',)

admin.site.register(DataPoint, DataPointAdmin)
admin.site.register(AllowedIPs, AllowedIPsAdmin)