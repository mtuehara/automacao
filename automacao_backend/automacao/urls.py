"""automacao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from med_labsoft import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/labprog/year_per_month/$', views.med_labprog_consume_of_the_year_by_month),
    url(r'^api/labprog/day_per_hour/$', views.med_labprog_daily_consume),
    url(r'^api/labprog/monthly_cost/$', views.med_labprog_monthly_cost),
    url(r'^api/labsoft/year_per_month/$', views.med_labsoft_consume_of_the_year_by_month),
    url(r'^api/labsoft/day_per_hour/$', views.med_labsoft_daily_consume),
    url(r'^api/labsoft/monthly_cost/$', views.med_labsoft_monthly_cost),
    url(r'^api/solar/day_per_hour/$', views.med_solar_daily_production),
    url(r'^api/solar/month_production/$', views.med_solar_month_production),
    url(r'^api/solar/year_production/$', views.med_solar_year_production),
    url(r'^api/solar/economy/$', views.med_solar_economy),
]
