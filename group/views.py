from django.http import HttpResponse
from django.shortcuts import render


def group_view(request, group_id=None):
    return render(request, 'group/group.html', {'group_id': group_id})
    return HttpResponse(group_id)

