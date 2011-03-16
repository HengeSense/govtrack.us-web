# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),
    url(r'^(about|press|sources|advertising|developers|developers/downstream|developers/data)$', 'staticpage', name='staticpage'),
    url(r'^congress/members(?:/([A-Z]+)(?:/(\d+))?)?$', 'browsemembers', name='browsemembers'),
    url(r'^congress$', 'congress_home', name='congress_home'),
    url(r'^congress/spectrum$', 'political_spectrum', name='political_spectrum'),
	
	url(r'^embed/mapframe(?:\.xpd)?$', 'districtmapembed', name='districtmapembed'),
)

