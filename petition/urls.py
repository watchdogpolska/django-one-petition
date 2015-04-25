from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.SignatureCreate.as_view(), name="create"),
    url(r'^new/$', views.SignatureList.as_view(), name='list'),
    url(r'^api/$', views.SignatureApiList.as_view(), name='list_api'),

    url(r'^thank-you/$', views.SignatureCreateDone.as_view(), name="thank-you"),

)
