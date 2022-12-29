from django.shortcuts import render
from .models import *
from datetime import timedelta,datetime
from pytz import timezone

def home_view(request):
    project = [1000,2000,3000] if not request.GET.get('project') else [int(project) for project in request.GET.get('project').split(',')]
    today = timezone('Asia/Ho_Chi_Minh').localize(datetime.now())
    date_time = (today-timedelta(days=7),today) if request.GET.get('updateStatus')=='inprocess' \
                else (today-timedelta(days=60),today-timedelta(days=10)) if request.GET.get('updateStatus')=='pending' else (today-timedelta(days=365),today)
    status = [1,2,3,4,5,6,7,8] if not request.GET.get('status') else [int(status) for status in request.GET.get('status').split(',')]
    person = [57,58,52,10] if not request.GET.get('person') else [int(person) for person in request.GET.get('person').split(',')] 
    sort = '-updated_date' if not request.GET.get('sort') else request.GET.get('sort')
    filters = {
        'project__in' : project,
        'updated_date__range' : date_time,
        'status__in' : status,
        'person_in_charge__in' : person,
    }
    task_list = Task.objects.filter(**filters).order_by(sort)
    limit = 20 if not request.GET.get('limit') else (int(request.GET.get('limit')) if request.GET.get('limit') != 'nolimit' else len(task_list))
    limit_value = 20 if not request.GET.get('limit') else (int(request.GET.get('limit')) if request.GET.get('limit') != 'nolimit' else 'nolimit')
    data = []
    getGrands = lambda task_list : (task['grand'] for task in task_list)
    getParentList = lambda parent_list : (parent[0] for parent in parent_list['parent_and_child'])
    try:
        for i in range(limit):
            task = task_list[i]
            if parent_task := Task.objects.filter(pk=task.parent_task_id_id).first():
                if grand_task := Task.objects.filter(pk=parent_task.parent_task_id_id).first():
                    if grand_task in getGrands(data):
                        task_index = next(i for i,task in enumerate(getGrands(data)) if task == grand_task)
                        if parent_task in getParentList(data[task_index]):
                            data[task_index]['parent_and_child'][next(i for i,task in enumerate(getParentList(data[task_index])) if task == parent_task)].append(task)
                            continue
                        data[task_index]['parent_and_child'].append([parent_task,task])
                        continue
                    data.append({'grand':grand_task,'parent_and_child':[[parent_task,task]]})
                    continue
                if parent_task in getGrands(data):
                    task_index = next(i for i,task in enumerate(getGrands(data)) if task == parent_task)
                    if task not in getParentList(data[task_index]):
                        data[task_index]['parent_and_child'].append([task])
                    continue
            if task not in getGrands(data):
                data.append({'grand':task,'parent_and_child':[]})
    except IndexError:
        limit = len(task_list)
        limit_value = len(task_list)
    current_page = [None,'active',None] if request.GET.get('project')=='1000' else \
        ([None,None,'active'] if request.GET.get('project')=='2000' else ['active',None,None])
    
    context = {
        'data' : data,
        'path' : current_page,
        'title' : 'Management',
        'project_value' : ','.join(str(x) for x in project),
        'person_value' : ','.join(str(x) for x in person),
        'status_value' : ','.join(str(x) for x in status),
        'sort_value' : sort,
        'limit_value' : limit_value,
        'project' : ','.join([x.project for x in Project.objects.filter(pk__in=project)]),
        'person' : Person.objects.filter(pk=person[0])[0].name if len(person)<2 else 'All' ,
        'status' : Task_Status.objects.filter(pk=status[0])[0].status if len(status)<2 else ('All' if len(person) == 8 else ''),
        'sort' : sort,
        'limit' : limit,
        'today' : today
    }
    return render(request,'main/home.html',context)

def task_view(request,pk):
    task = Task.objects.get(pk=pk)
    parent_task = task.parent_task_id
    child_task = Task.objects.filter(parent_task_id=task)
    log_times = LogTime.objects.filter(task_id=task).order_by('-created_date')
    context = {
        'task' : task,
        'parent_task' : parent_task,
        'child_task' : child_task,
        'log_times' : log_times
    }
    return render(request,'main/task.html',context)