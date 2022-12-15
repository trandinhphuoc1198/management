from django.shortcuts import render
from .models import Task
from django.core.paginator import Paginator

def home_view(request):
    limit = 11
    task_list = Task.objects.all().order_by('-updated_date')
    data = []

    for i in range(limit):
        print(data)
        loop_must_stop = False
        task = task_list[i]
        print(task,i)

        if task.parent_task_id:
            parent_task = Task.objects.filter(pk=task.parent_task_id_id).first()

            if parent_task.parent_task_id:
                grand_task = Task.objects.filter(pk=parent_task.parent_task_id_id).first()
                for added_task in data:
                    if grand_task == added_task['grand']:
                        for added_parent_task in added_task['parent_and_child']:
                            if parent_task == added_parent_task[0]:
                                added_parent_task.append(task)
                                loop_must_stop = True
                                break
                        if loop_must_stop: break
                        added_task['parent_and_child'].append([parent_task,task])
                        loop_must_stop = True
                        break
                if loop_must_stop: break
                data.append({'grand': grand_task, 'parent_and_child' : [[parent_task,task]]})
                loop_must_stop = True
                break
            if loop_must_stop: break
            for added_task in data:
                if parent_task == added_task['grand']:
                    added_task['parent_and_child'].append([task])
                    loop_must_stop = True
                    break
            if loop_must_stop: continue
            data.append({'grand':parent_task,'parent_and_child':[[task]]})
            continue
        for added_task in data:
            if task == added_task['grand']:
                loop_must_stop = True
                break
        if loop_must_stop: continue
        data.append({'grand':task,'parent_and_child':[]})

    


    return render(request,'main/home.html',{'data': data})

# def project_view(request,project):
#     project=[1,2]
#     if project:
#         project = [1] if project=='shiten' else [2]
#     limit = 2
#     task_list = Task.objects.filter(project__in=project).order_by('-updated_date')[:limit]
#     total_task_to_show = []

#     for i in range(limit):
#         task = task_list[i]
#         if task.parent_task_id:
#             parent_task = Task.objects.filter(pk=task.parent_task_id_id).first()
#             if parent_task.parent_task_id:
#                 grand_task = Task.objects.filter(pk=parent_task.parent_task_id_id).first()

#     return render(request,'main/home.html')