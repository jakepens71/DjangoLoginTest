from django.conf.urls import patterns, url, include
from rango.views import RangoIndex

urlpatterns = patterns('',
        url(r'^$', 'rango.views.index'),
        url(r'^about/$', 'rango.views.about'),
        url(r'^index_class/$', RangoIndex.as_view()),
        url(r'^register/$', 'rango.views.register'),
                       )
