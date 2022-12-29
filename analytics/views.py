from django.shortcuts import render
from main.models import Task,LogTime,Person
from django.db.models import Sum
import json
from datetime import datetime,timedelta
from pytz import timezone

def project_time_spent(request):
    tz = timezone('Asia/Ho_Chi_Minh')
    time_start = datetime.now() - timedelta(days=30) if not request.GET.get('time_start') else datetime.strptime(request.GET.get('time_start'),'%Y-%m-%d')
    time_end = datetime.now() if not request.GET.get('time_end') else datetime.strptime(request.GET.get('time_end'),'%Y-%m-%d')
    if time_end < time_start:
        return 
    data = LogTime.objects.filter(created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id__project').annotate(spent_time=Sum('spent_time')).order_by('task_id__project')

    spent_time_list = {}
    for i in data:
        spent_time_list.update({str(i['task_id__project']) : i['spent_time']})
    print(spent_time_list)
    shiten_task_sum = LogTime.objects.filter(task_id__project_id=1000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()
    grs_task_sum = LogTime.objects.filter(task_id__project_id=2000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()
    other_task_sum = LogTime.objects.filter(task_id__project_id=3000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()

    shiten_spent_time = LogTime.objects.filter(task_id__project_id=1000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').annotate(spent_time=Sum('spent_time')).order_by('task_id')
    grs_spent_time = LogTime.objects.filter(task_id__project_id=2000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').annotate(spent_time=Sum('spent_time')).order_by('task_id')
    other_spent_time = LogTime.objects.filter(task_id__project_id=3000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').annotate(spent_time=Sum('spent_time')).order_by('task_id')
    shiten_tasks = Task.objects.filter(pk__in=[task_id['task_id'] for task_id in shiten_spent_time]).order_by('id')
    grs_tasks = Task.objects.filter(pk__in=[task_id['task_id'] for task_id in grs_spent_time]).order_by('id')
    other_tasks = Task.objects.filter(pk__in=[task_id['task_id'] for task_id in other_spent_time]).order_by('id')
    tasks_detail = {
        'shiten' : sorted(zip(shiten_tasks,[shiten['spent_time'] for shiten in shiten_spent_time]),key= lambda x : x[1],reverse=True),
        'grs' : sorted(zip(grs_tasks,[grs['spent_time'] for grs in grs_spent_time]),key= lambda x : x[1],reverse=True),
        'other' : sorted(zip(other_tasks,[other['spent_time'] for other in other_spent_time]),key= lambda x : x[1],reverse=True),
    }
    context = {
        'data': json.dumps(spent_time_list) , 
        'data2': spent_time_list,
        'title' : 'Analytics',
        'time_range': f"{time_end.strftime('%d-%m-%Y')} => {time_end.strftime('%d-%m-%Y')}" ,
        'time_end':time_end.strftime('%Y-%m-%d'),
        'time_start':time_start.strftime('%Y-%m-%d'),
        'shiten_task_sum':shiten_task_sum,
        'grs_task_sum':grs_task_sum,
        'other_task_sum':other_task_sum,
        'tasks_detail' : tasks_detail
        }
    return render(request,'analytics/project.html',context)


def project_time_spent_by_person(request,person):
    tz = timezone('Asia/Ho_Chi_Minh')
    time_start = datetime.now() - timedelta(days=30) if not request.GET.get('time_start') else datetime.strptime(request.GET.get('time_start'),'%Y-%m-%d')
    time_end = datetime.now() if not request.GET.get('time_end') else datetime.strptime(request.GET.get('time_end'),'%Y-%m-%d')
    if time_end < time_start:
        return 
    data = LogTime.objects.filter(person=person,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id__project').annotate(spent_time=Sum('spent_time')).order_by('task_id__project')

    spent_time_list = {}
    for i in data:
        spent_time_list.update({str(i['task_id__project']) : i['spent_time']})
    print(spent_time_list)
    shiten_task_sum = LogTime.objects.filter(person=person,task_id__project_id=1000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()
    grs_task_sum = LogTime.objects.filter(person=person,task_id__project_id=2000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()
    other_task_sum = LogTime.objects.filter(person=person,task_id__project_id=3000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()

    shiten_spent_time = LogTime.objects.filter(person=person,task_id__project_id=1000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').annotate(spent_time=Sum('spent_time')).order_by('task_id')
    grs_spent_time = LogTime.objects.filter(person=person,task_id__project_id=2000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').annotate(spent_time=Sum('spent_time')).order_by('task_id')
    other_spent_time = LogTime.objects.filter(person=person,task_id__project_id=3000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').annotate(spent_time=Sum('spent_time')).order_by('task_id')
    shiten_tasks = Task.objects.filter(pk__in=[task_id['task_id'] for task_id in shiten_spent_time]).order_by('id')
    grs_tasks = Task.objects.filter(pk__in=[task_id['task_id'] for task_id in grs_spent_time]).order_by('id')
    other_tasks = Task.objects.filter(pk__in=[task_id['task_id'] for task_id in other_spent_time]).order_by('id')
    tasks_detail = {
        'shiten' : sorted(zip(shiten_tasks,[shiten['spent_time'] for shiten in shiten_spent_time]),key= lambda x : x[1],reverse=True),
        'grs' : sorted(zip(grs_tasks,[grs['spent_time'] for grs in grs_spent_time]),key= lambda x : x[1],reverse=True),
        'other' : sorted(zip(other_tasks,[other['spent_time'] for other in other_spent_time]),key= lambda x : x[1],reverse=True),
    }
    context = {
        'data': json.dumps(spent_time_list) , 
        'data2': spent_time_list,
        'title' : 'Analytics',
        'time_range': f"{time_end.strftime('%d-%m-%Y')} => {time_end.strftime('%d-%m-%Y')}" ,
        'time_end':time_end.strftime('%Y-%m-%d'),
        'time_start':time_start.strftime('%Y-%m-%d'),
        'shiten_task_sum':shiten_task_sum,
        'grs_task_sum':grs_task_sum,
        'other_task_sum':other_task_sum,
        'tasks_detail' : tasks_detail,
        'person' : Person.objects.get(pk=person)
        }
    return render(request,'analytics/project.html',context)