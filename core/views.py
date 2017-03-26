from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'base.html')


def error404(request):
    return HttpResponse(404)


def groups(request):
    groups = [
        "123",
        "345",
        "567"
    ]
    return render(request, 'core/groups_view.html', {"groups": groups})



