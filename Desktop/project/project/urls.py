"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from gps import views
from rest_framework import routers


"""router=routers.DefaultRouter()
router.register(r'gps',views.locationview)"""

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gps/', views.locationview.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.locationdetail.as_view()),
url(r'^gps/(?P<pk>[0-9]+)/$', views.locationview.as_view()),

)



"""urlpatterns = [

url(r'^admin/', admin.site.urls),
url(r'^',include(router.urls)),



]"""
"""urlpatterns = format_suffix_patterns(urlpatterns)
url(r'^$', views.locationview.as_view()),"""