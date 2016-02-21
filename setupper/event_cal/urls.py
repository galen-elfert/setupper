from django.conf.urls import url
import datetime

from . import views

today = datetime.date.today()


app_name = 'event_cal'
urlpatterns = [
    # eg: /event_cal/
    url(r'^$', views.event_cal, name='index'),
    # eg: /event_cal/HCC/2016/02/25
    url(r'^(?P<building>[\w]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$', views.event_cal, name='event_cal_full'),
    # eg: /event_cal/HCC/  (no date, should default to today)
    url(r'^(?P<building>[\w]+)/$', views.event_cal, {'year': today.year, 'month': today.month, 'day': today.day}, name='event_cal_short'),
]
