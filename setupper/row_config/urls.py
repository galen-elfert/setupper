from django.conf.urls import url

from . import views

app_name = 'row_config'
urlpatterns = [
    # Goes to building selection screen
    url(r'^$', views.row_config, name='index'),
    
    url(r'^(?P<building>[\w]+)/$', views.row_config, name='row_config')
]
