from rest_framework import viewsets
from rest_framework.generics import mixins
from tracks.serializers import DataPointSerializer
from tracks.models import DataPoint
from django.shortcuts import render
import string
import random
from tracks.permissions import TracksPermission
from django.db.models import Count
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class ReadOnlyModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, and 'list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class WriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides`create` action.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class ReadWriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A viewset that provides `retrieve`, 'list`, and `create` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class DataPointViewSet(WriteOnlyModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer


class ReadDataPointViewSet(ReadOnlyModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    permission_classes = [TracksPermission]


def show_user_code(request):
    this_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    context = {'this_code': this_code}
    return render(request, 'tracks/get_user_code.html', context)


def download_fix_stats(request):
    if request.user.is_authenticated() and 'stats_access' in [group.name for group in request.user.groups.all()]:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="fix_stats.csv"'
        writer = csv.writer(response)
        writer.writerow(['user_code', 'n_fixes'])
        fix_counts = DataPoint.objects.filter(type="FIX").values('user_code').annotate(n_fixes=Count('user_code'))
        for u in fix_counts:
            writer.writerow([u['user_code'], u['n_fixes']])
        return response
    else:
        return HttpResponseRedirect(reverse('auth_login'))


def download_reg_stats(request):
    if request.user.is_authenticated() and 'stats_access' in [group.name for group in request.user.groups.all()]:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="reg_stats.csv"'
        writer = csv.writer(response)
        writer.writerow(['user_code', 'registration_upload_time'])
        reg = DataPoint.objects.filter(type="REG")
        for r in reg:
            writer.writerow([r.user_code, r.created.strftime("%d/%m/%Y")])
        return response
    else:
        return HttpResponseRedirect(reverse('auth_login'))


