"""loganalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loganalyzerapp import views
from django.conf.urls.static import settings,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_view),
    path('form/',views.form_view),
    path('monitor/',views.monitor_view),
    #path('monitor/onload_details',views.getmonitr_path),
    #path('monitor/ip_adress',views.ip_adress),
    path('monitor/filter_data_with_ip_address',views.filter_data_with_ip_address),
    path('monitor/get_data',views.get_values_view),
    path('monitor/update_new_data',views.update_DB),
    path('report/',views.report_view),
    path('report/groupby_Ipadress',views.groupby_Ipadress)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
