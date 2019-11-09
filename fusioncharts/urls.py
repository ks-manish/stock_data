"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from fusioncharts.views import catalogue, chart

from fusioncharts import datahandler
from fusioncharts.samples import Line_Chart_With_Time_Axis, Plotting_Multiple_Series_On_Time_Axis


urlpatterns = [
    url(r'^$', catalogue),
    url(r'^admin/', admin.site.urls),
    url(r'^datahandler', datahandler.getdata),
    url(r'^Line-Chart-With-Time-Axis', Line_Chart_With_Time_Axis.chart, name='chart'),
    url(r'^Plotting-Multiple-Series-On-Time-Axis', Plotting_Multiple_Series_On_Time_Axis.chart, name='chart'),
]