#  from django.conf.urls import url
from . import views
from django.urls import path

from django.urls import path
# from knox import views as knox_views


urlpatterns = [
    # path('api/login', views.login),
    # path('api/time', views.Time.as_view(), name='getDate'),
    # path('api/sampleapi', views.sample_api),
    path('', views.favicon, name='favicon'),  # website
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]