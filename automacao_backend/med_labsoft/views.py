from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from django.utils import timezone
import pytz
import calendar
import random

from .models import MedLabprog, MedLabsoft, MedSolar
from django.shortcuts import render

energy_cost = []
for i in range(12):
    energy_cost.append(random.uniform(0.55, 0.60))

# Create your views here.
@api_view(['PUT'])
def med_labprog_consume_of_the_year_by_month(request):
    if request.method == 'PUT':
        year = request.data['data']['year']
        # next_year = year + 1
        # per_month = []
        # for month in range(1, 13):
        #     monthly_sum = 0
        #     dt_month = datetime(year, month, 1, tzinfo=pytz.UTC)
        #     if(month == 12):
        #         next_month = 1
        #         dt_next_month = datetime(next_year, next_month, 1, tzinfo=pytz.UTC)
        #     else:
        #         next_month = month + 1
        #         dt_next_month = datetime(year, next_month, 1, tzinfo=pytz.UTC)            
        #     month_query = MedLabprog.objects.filter(tempo__range=[dt_month, dt_next_month]).order_by('id')
        #     for index in range(len(month_query)):
        #         if(index == len(month_query)-1):
        #             time = 5/3600
        #         else:
        #             time = (month_query[index+1].tempo - month_query[index].tempo).total_seconds()
        #             time = abs(time/3600)
        #         monthly_sum += (time * month_query[index].total)
        #     per_month.append(monthly_sum/1000)
        if(year==2019):
            per_month = [
                0.0,
                431.1702010410704,
                695.7322507597303,
                645.886586450022,
                304.7594548950906,
                173.24127103111832,
                168.98649096072225,
                299.9662396122702,
                544.4680842331259,
                771.5707189502851,
                255.46022979261085,
                0.0
            ]
        elif(year==2020):
            per_month = [
                101.75200829260518,
                0.0,
                96.93661612731125,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ]
        else:
            per_month = []
        return Response({
            'data': per_month
        })

@api_view(['PUT'])
def med_labsoft_consume_of_the_year_by_month(request):
    if request.method == 'PUT':
        year = request.data['data']['year']
        # next_year = year + 1
        # per_month = []
        # for month in range(1, 13):
        #     monthly_sum = 0
        #     dt_month = datetime(year, month, 1, tzinfo=pytz.UTC)
        #     if(month == 12):
        #         next_month = 1
        #         dt_next_month = datetime(next_year, next_month, 1, tzinfo=pytz.UTC)
        #     else:
        #         next_month = month + 1
        #         dt_next_month = datetime(year, next_month, 1, tzinfo=pytz.UTC)            
        #     month_query = MedLabsoft.objects.filter(tempo__range=[dt_month, dt_next_month]).order_by('id')
        #     for index in range(len(month_query)):
        #         if(index == len(month_query)-1):
        #             time = 5/3600
        #         else:
        #             time = (month_query[index+1].tempo - month_query[index].tempo).total_seconds()
        #             time = abs(time/3600)
        #         monthly_sum += (time * month_query[index].total)
        #     per_month.append(monthly_sum/1000)
        if(year==2019):
            per_month = [
                    0.0,
                    382.22388742988767,
                    662.3745453840368,
                    692.7642762858418,
                    370.1129712903796,
                    165.5470971795756,
                    181.31427975340807,
                    160.30666263470673,
                    485.77719512464586,
                    398.7537387822664,
                    276.6849997259996,
                    0.0
                ]
        elif(year==2020):
            per_month = [
                    150.7086100692642,
                    0.0,
                    480.4630593182864,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ]
        else:
            per_month = []
        return Response({
            'data': per_month
        })

@api_view(['PUT'])
def med_labprog_daily_consume(request):
    if request.method == 'PUT':
        start_day = request.data['data']['day']
        start_month = request.data['data']['month']
        start_year = request.data['data']['year']
        last_day_of_the_month = calendar.monthrange(start_year, start_month)[1]
        if(start_day == last_day_of_the_month):
            end_day = 1
            if(month != 12):
                end_month = month + 1
                end_year = start_year
            else:
                end_month = 1
                end_year = start_year + 1
        else:
            end_day = start_day + 1
            end_month = start_month
            end_year = start_year

        dt_start = datetime(start_year, start_month, start_day, tzinfo=pytz.UTC)
        dt_end = datetime(end_year, end_month, end_day, tzinfo=pytz.UTC)

        queryset = MedLabprog.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
        per_hour = []

        for hour in range(24):
            hourly_sum = 0
            start_hour = hour
            if(hour == 23):
                end_min = 59
                end_sec = 59
            else:
                end_hour = hour + 1
                end_min = 0
                end_sec = 0
            dt_start = datetime(start_year, start_month, start_day, start_hour, tzinfo=pytz.UTC)
            dt_end = datetime(start_year, start_month, start_day, end_hour, end_min, end_sec, tzinfo=pytz.UTC)
            hourly_query = queryset.filter(tempo__range=[dt_start, dt_end]).order_by('id')
            for index in range(len(hourly_query)):
                if(index == len(hourly_query)-1):
                    time = 5/3600
                else:
                    time = (hourly_query[index+1].tempo - hourly_query[index].tempo).total_seconds()
                    time = abs(time/3600)
                hourly_sum += (time * hourly_query[index].total)
            per_hour.append(hourly_sum/1000)

        return Response({
            'data': per_hour
        })

@api_view(['PUT'])
def med_labsoft_daily_consume(request):
    if request.method == 'PUT':
        start_day = request.data['data']['day']
        start_month = request.data['data']['month']
        start_year = request.data['data']['year']
        last_day_of_the_month = calendar.monthrange(start_year, start_month)[1]
        if(start_day == last_day_of_the_month):
            end_day = 1
            if(month != 12):
                end_month = month + 1
                end_year = start_year
            else:
                end_month = 1
                end_year = start_year + 1
        else:
            end_day = start_day + 1
            end_month = start_month
            end_year = start_year

        dt_start = datetime(start_year, start_month, start_day, tzinfo=pytz.UTC)
        dt_end = datetime(end_year, end_month, end_day, tzinfo=pytz.UTC)

        queryset = MedLabsoft.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
        per_hour = []

        for hour in range(24):
            hourly_sum = 0
            start_hour = hour
            if(hour == 23):
                end_min = 59
                end_sec = 59
            else:
                end_hour = hour + 1
                end_min = 0
                end_sec = 0
            dt_start = datetime(start_year, start_month, start_day, start_hour, tzinfo=pytz.UTC)
            dt_end = datetime(start_year, start_month, start_day, end_hour, end_min, end_sec, tzinfo=pytz.UTC)
            hourly_query = queryset.filter(tempo__range=[dt_start, dt_end]).order_by('id')
            for index in range(len(hourly_query)):
                if(index == len(hourly_query)-1):
                    time = 5/3600
                else:
                    time = (hourly_query[index+1].tempo - hourly_query[index].tempo).total_seconds()
                    time = abs(time/3600)
                hourly_sum += (time * hourly_query[index].total)
            per_hour.append(hourly_sum/1000)

        return Response({
            'data': per_hour
        })

@api_view(['PUT'])
def med_labprog_monthly_cost(request):
    global energy_cost
    if request.method == 'PUT':
        start_month = request.data['data']['month']
        start_year = request.data['data']['year']
        if(start_month == 12):
            end_month = 1
            end_year = start_year + 1
        else:
            end_month = start_month + 1
            end_year = start_year

        dt_start = datetime(start_year, start_month, 1, tzinfo=pytz.UTC)
        dt_end = datetime(end_year, end_month, 1, tzinfo=pytz.UTC)

        queryset = MedLabprog.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
        consume = 0

        for index in range(len(queryset)):
            if(index == len(queryset)-1):
                time = 5/3600
            else:
                time = (queryset[index+1].tempo - queryset[index].tempo).total_seconds()
                time = abs(time/3600)
            consume += (time * queryset[index].total/1000)
        
        month_energy_cost = energy_cost[start_month-1]
        monthly_cost = consume * month_energy_cost

        return Response({
            'data': {
                'consume': consume,
                'monthly_cost': monthly_cost
            }
        })

@api_view(['PUT'])
def med_labsoft_monthly_cost(request):
    global energy_cost
    if request.method == 'PUT':
        start_month = request.data['data']['month']
        start_year = request.data['data']['year']
        # if(start_month == 12):
        #     end_month = 1
        #     end_year = start_year + 1
        # else:
        #     end_month = start_month + 1
        #     end_year = start_year

        # dt_start = datetime(start_year, start_month, 1, tzinfo=pytz.UTC)
        # dt_end = datetime(end_year, end_month, 1, tzinfo=pytz.UTC)

        # queryset = MedLabsoft.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
        # consume = 0

        # for index in range(len(queryset)):
        #     if(index == len(queryset)-1):
        #         time = 5/3600
        #     else:
        #         time = (queryset[index+1].tempo - queryset[index].tempo).total_seconds()
        #         time = abs(time/3600)
        #     consume += (time * queryset[index].total/1000)

        # month_energy_cost = energy_cost[start_month-1]
        # monthly_cost = consume * month_energy_cost
        if(start_year==2019):
            per_month = [
                    0.0,
                    382.22388742988767,
                    662.3745453840368,
                    692.7642762858418,
                    370.1129712903796,
                    165.5470971795756,
                    181.31427975340807,
                    160.30666263470673,
                    485.77719512464586,
                    398.7537387822664,
                    276.6849997259996,
                    0.0
                ]
        elif(start_year==2020):
            per_month = [
                    150.7086100692642,
                    0.0,
                    480.4630593182864,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ]
        return Response({
            'data': {
                'consume': per_month[start_month-1],
                'monthly_cost': per_month[start_month-1]*energy_cost[start_month-1]
            }
        })

@api_view(['PUT'])
def med_solar_daily_production(request):
    if request.method == 'PUT':
        start_day = request.data['data']['day']
        start_month = request.data['data']['month']
        start_year = request.data['data']['year']

        dt_start = datetime(start_year, start_month, start_day, tzinfo=pytz.UTC)
        dt_end = datetime(start_year, start_month, start_day, 23, 59, 59, tzinfo=pytz.UTC)

        queryset = MedSolar.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
        per_hour = []

        for item in queryset:
            obj = {
                'hour': item.tempo.hour,
                'production': item.total
            }
            per_hour.append(obj)            

        return Response({
            'data': per_hour
        })

@api_view(['PUT'])
def med_solar_month_production(request):
    if request.method == 'PUT':
        month = request.data['data']['month']
        year = request.data['data']['year']
        last_day_of_the_month = calendar.monthrange(year, month)[1]
        data = []
        for day in range(1, last_day_of_the_month+1):
            dt_start = datetime(year, month, day, tzinfo=pytz.UTC)
            dt_end = datetime(year, month, day, 23, 59, 59, tzinfo=pytz.UTC)
            queryset = MedSolar.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
            daily_production = 0
            for item in queryset:
                daily_production += item.total
            obj = {
                'day': day,
                'production': daily_production
            }
            data.append(obj)

        return Response({
            'data': data
        })

@api_view(['PUT'])
def med_solar_year_production(request):
    if request.method == 'PUT':
        start_year = request.data['data']['year']
        per_month = []
        for start_month in range(1, 13):
            if(start_month != 12):
                end_month = start_month + 1
                end_year = start_year
            else:
                end_month = 1
                end_year = start_year + 1

            dt_start = datetime(start_year, start_month, 1, tzinfo=pytz.UTC)
            dt_end = datetime(end_year, end_month, 1, tzinfo=pytz.UTC)

            queryset = MedSolar.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
            monthly_production = 0
            for item in queryset:
                monthly_production += item.total
            obj = {
                'month': start_month,
                'production': monthly_production
            }
            per_month.append(obj) 

        return Response({
            'data': per_month
        })


@api_view(['PUT'])
def med_solar_economy(request):
    global energy_cost
    if request.method == 'PUT':
        start_year = request.data['data']['year']
        per_month = []
        for start_month in range(1, 13):
            month_energy_cost = energy_cost[start_month-1]
            if(start_month != 12):
                end_month = start_month + 1
                end_year = start_year
            else:
                end_month = 1
                end_year = start_year + 1

            dt_start = datetime(start_year, start_month, 1, tzinfo=pytz.UTC)
            dt_end = datetime(end_year, end_month, 1, tzinfo=pytz.UTC)

            queryset = MedSolar.objects.filter(tempo__range=[dt_start, dt_end]).order_by('id')
            monthly_production = 0
            for item in queryset:
                monthly_production += item.total
            obj = {
                'month': start_month,
                'economy': monthly_production*0.60*month_energy_cost
            }
            per_month.append(obj) 

        return Response({
            'data': per_month
        })
