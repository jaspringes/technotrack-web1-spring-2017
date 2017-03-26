from django.conf.urls import url
from group.views import group_view


urlpatterns = [
    url(r'(?P<group_id>\d+)/', group_view),
    #url(r'(?P<group_id>\d+)/', groups)
]

