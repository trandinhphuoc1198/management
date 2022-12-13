from django.shortcuts import render
from .models import Task
from django.core.paginator import Paginator

def home_view(request):
    limit = 10
    task_list = Task.objects.all().order_by('-updated_date')
    data = dict()
    skip_data = []

    for i in range(limit):
        task = task_list[i]
        try:
            skip_data.index(task)
        except:
            print(task.id)
            data[task] = {}

            # if task.parent_task_id:
            #     parent_task = Task.objects.filter(pk=task.parent_task_id_id).first()
            #     if data.get(parent_task):
            #         data[parent_task].add(task)
            #     else:
            #         data[parent_task] = {task}
            #     del data[task]
            #     skip_data.append(parent_task)

            #     if parent_task.parent_task_id:
            #         grand_task = Task.objects.filter(pk=parent_task.parent_task_id_id).first()
            #         data[grand_task] = {data[parent_task]}
            #         del data[parent_task]
            #         skip_data.append(grand_task)
                    
            # skip_data.append(task)



    return render(request,'main/home.html',{'data':{'a':task}})

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