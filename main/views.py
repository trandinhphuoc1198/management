from django.shortcuts import render
from .models import Task
from datetime import timedelta,datetime
from pytz import timezone

def home_view(request,project=None):
    project = [1000] if request.path == '/top/shiten' else ([2000] if request.path == '/top/grs' else [1000,2000])
    today = timezone('Asia/Ho_Chi_Minh').localize(datetime.now())
    date_time = (today-timedelta(days=7),today) if request.GET.get('updateStatus')=='inprocess' \
                else (today-timedelta(days=30),today-timedelta(days=7)) if request.GET.get('updateStatus')=='pending' else (today-timedelta(days=365),today)
    status = [1,2,3,4,5,6,7,8] if request.GET.get('status')=='inprocess' else ([3] if request.GET.get('status')=='pending' else ([4]if request.GET.get('status')=='finished' else[1,2,3,4,5,6,7,8]))
    person = [57,58,52,10] if not request.GET.get('person') else ([1] if request.GET.get('person')=='phuong' else [2])
    limit = int(request.GET.get('limit')) if request.GET.get('limit') else 100
    filters = {
        'project__in' : project,
        'updated_date__range' : date_time,
        'status__in' : status,
        'person_in_charge__in' : person,
    }
    task_list = Task.objects.filter(**filters)
    print(filters)
    data = []
    getGrands = lambda task_list : (task['grand'] for task in task_list)
    getParentList = lambda parent_list : (parent[0] for parent in parent_list['parent_and_child'])
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
    current_page = [None,'active',None] if 'shiten' in request.path else \
        ([None,None,'active'] if 'grs' in request.path else ['active',None,None])
    context = {
        'data' : data,
        'path' : current_page
    }
    return render(request,'main/home.html',context)
