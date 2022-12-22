from django.shortcuts import render
from main.models import Task,LogTime
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
    shiten_tasks = LogTime.objects.filter(task_id__project_id=1000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()
    grs_tasks = LogTime.objects.filter(task_id__project_id=2000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()
    other_tasks = LogTime.objects.filter(task_id__project_id=3000,created_date__range=(tz.localize(time_start),tz.localize(time_end))).values('task_id').distinct()

    context = {
        'data': json.dumps(spent_time_list) , 
        'data2': spent_time_list,
        'title' : 'Analytics',
        'time_range': f"{time_end.strftime('%d-%m-%Y')} => {time_end.strftime('%d-%m-%Y')}" ,
        'time_end':time_end.strftime('%Y-%m-%d'),
        'time_start':time_start.strftime('%Y-%m-%d'),
        'shiten_tasks':shiten_tasks,
        'grs_tasks':grs_tasks,
        'other_tasks':other_tasks}
    return render(request,'analytics/home.html',context)