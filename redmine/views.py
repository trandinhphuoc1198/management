from main.models import *
from .models import *
from django.http import HttpResponse
from datetime import datetime,timedelta
from pytz import timezone
from django.db import IntegrityError

Shiten = 1000
Garage_Sales = 2000
Other = 3000
WebikeGarageSale = 48
MarketPlace_Staff_Tool = 49
MarketPlace_API = 50
MarketPlace = 51
RBM_B = 4
RC_BranchManager = 5
Common_Project = 17

def sync_meta_data(request):
    try:
        projects_from_redmine = Projects.objects.all()
        projects_to_management = []
        for project in projects_from_redmine:
            projects_to_management.append(Project(id=project.id,project=project.name))
        Project.objects.bulk_create(projects_to_management,update_conflicts=True,update_fields=['project'])

        persons_from_redmine = Users.objects.all()
        persons_to_management = []
        for person in persons_from_redmine:
            persons_to_management.append(Person(id=person.id,name=f'{person.lastname}'))
        Person.objects.bulk_create(persons_to_management,update_conflicts=True,update_fields=['name'])

        task_statuses_from_redmine = IssueStatuses.objects.all()
        task_statuses_to_management = []
        for task_status in task_statuses_from_redmine:
            task_statuses_to_management.append(Task_Status(id=task_status.id,status=task_status.name))
        Task_Status.objects.bulk_create(task_statuses_to_management,update_conflicts=True,update_fields=['status'])

        task_types_from_redmine = Trackers.objects.all()
        task_types_to_management = []
        for task_type in task_types_from_redmine:
            task_types_to_management.append(Task_Type(id=task_type.id,type=task_type.name))
        Task_Type.objects.bulk_create(task_types_to_management,update_conflicts=True,update_fields=['type'])

        activities_from_redmine = Enumerations.objects.all()
        activities_to_management = []
        for activity in activities_from_redmine:
            activities_to_management.append(Activity(id=activity.id,activity=activity.name))
        Activity.objects.bulk_create(activities_to_management,update_conflicts=True,update_fields=['activity'])

        categories_to_management =[
            Task_Category(id=17,category='Common Project',project_id=3000),
            Task_Category(id=4,category='RBM&B',project_id=1000),
            Task_Category(id=5,category='RBM',project_id=1000),
            Task_Category(id=52,category='RBM-Batch',project_id=1000),
            Task_Category(id=48,category='WebikeGarageSale',project_id=2000),
            Task_Category(id=49,category='MarketPlace_Staff_Tool',project_id=2000),
            Task_Category(id=50,category='MarketPlace_API',project_id=2000),
            Task_Category(id=51,category='MarketPlace',project_id=2000),
            Task_Category(id=56,category='Rakuten Contact Us',project_id=1000,category_parent_id=52),
            Task_Category(id=57,category='Rakuten Order',project_id=1000,category_parent_id=52),
            Task_Category(id=58,category='Rakuten Product',project_id=1000,category_parent_id=52),
            Task_Category(id=59,category='Yahoo Contact Us',project_id=1000,category_parent_id=52),
            Task_Category(id=60,category='Yahoo Product',project_id=1000,category_parent_id=52),
            Task_Category(id=61,category='Yahoo Order',project_id=1000,category_parent_id=52),
            Task_Category(id=62,category='Other',project_id=1000,category_parent_id=52)
        ]
        Task_Category.objects.bulk_create(categories_to_management,update_conflicts=True,update_fields=['category'])
        
        return HttpResponse('Sync meta data success')
    except Exception as e:
        return HttpResponse(e)


def sync_task(request,days=7):
    days=int(days)
    tz = timezone('Asia/Ho_Chi_Minh')
    point_of_time_to_sync = tz.localize(datetime.now() - timedelta(days=days))
    taskes_from_redmine = Issues.objects.filter(updated_on__gte=point_of_time_to_sync).order_by('created_on')
    taskes_to_management = []
    for task in taskes_from_redmine:
        project_id = Garage_Sales if task.project_id in [MarketPlace_Staff_Tool,MarketPlace_API,MarketPlace,WebikeGarageSale] \
                    else (Shiten if task.project_id != Common_Project else Other)
        category_id = task.category_id if task.category_id else task.project_id
        taskes_to_management.append({
                'id' : task.id,
                'task_title' : task.subject,
                'status_id' : task.status_id,
                'done_ratio' : task.done_ratio,
                'parent_task_id_id' : task.parent_id,
                'description' : task.description,
                'target_date' :task.due_date,
                'type_id' : task.tracker_id,
                'priority' : task.priority_id,
                'person_in_charge_id' : task.assigned_to_id,
                'project_id' : project_id,
                'category_id' : category_id,
                'note' : '',
                'spent_time' : 0,
                'estimate_time' : task.estimated_hours,
                'created_date' : task.created_on,
                'updated_date' : task.updated_on
            })
    retry = True
    while retry:
        retry = False
        for task in taskes_to_management:
            try:
                Task.objects.update_or_create(pk=task['id'],defaults=task)
            except IntegrityError as e:
                sync_specified_task(request,task['parent_task_id_id'])
            except Exception as e:
                print('=============',task['id'],'==============')
                return HttpResponse(e)
    return HttpResponse('Sync task success!')

def sync_specified_task(request,id=None):
    print(id)
    task_from_redmine = Issues.objects.get(pk=id)
    
    project_id = Garage_Sales if task_from_redmine.project_id in [MarketPlace_Staff_Tool,MarketPlace_API,MarketPlace,WebikeGarageSale] \
                    else (Shiten if task_from_redmine.project_id != Common_Project else Other)
    category_id = task_from_redmine.category_id if task_from_redmine.category_id else task_from_redmine.project_id
    while True:
        try:
            Task.objects.update_or_create(pk=id,defaults={
                    'id' : task_from_redmine.id,
                    'task_title' : task_from_redmine.subject,
                    'status_id' : task_from_redmine.status_id,
                    'done_ratio' : task_from_redmine.done_ratio,
                    'parent_task_id_id' : task_from_redmine.parent_id,
                    'description' : task_from_redmine.description,
                    'target_date' :task_from_redmine.due_date,
                    'type_id' : task_from_redmine.tracker_id,
                    'priority' : task_from_redmine.priority_id,
                    'person_in_charge_id' : task_from_redmine.assigned_to_id,
                    'project_id' : project_id,
                    'category_id' : category_id,
                    'note' : '',
                    'spent_time' : 0,
                    'estimate_time' : task_from_redmine.estimated_hours,
                    'created_date' : task_from_redmine.created_on,
                    'updated_date' : task_from_redmine.updated_on
                })
            return HttpResponse('Sync task success!')
        except IntegrityError:
            sync_specified_task(request,task_from_redmine.parent_id)
        except Exception as e:
            return HttpResponse(e)

def sync_logtime(request,days=7):
    days=int(days)
    print(days)

    tz = timezone('Asia/Ho_Chi_Minh')
    point_of_time_to_sync = tz.localize(datetime.now() - timedelta(days=days))
    logtimes_from_redmine = TimeEntries.objects.filter(updated_on__gte=point_of_time_to_sync).order_by('created_on')
    logtimes_to_management = []
    for logtime in logtimes_from_redmine:
        logtimes_to_management.append({
                'id' : logtime.id,
                'person_id' : logtime.user_id,
                'activity_id' : logtime.activity_id,
                'task_id_id' : logtime.issue_id,
                'spent_time' : logtime.hours,
                'comments' : logtime.comments,
                'created_date' : logtime.created_on,
                'updated_date' : logtime.updated_on
            })

    for logtime in logtimes_to_management:
        try:
            LogTime.objects.update_or_create(pk=logtime['id'],defaults=logtime)
        except IntegrityError:
            sync_specified_task(request,logtime['task_id_id'])
        except Exception as e:
            print('=============',logtime['id'],'==============')
            return HttpResponse(e)
    return HttpResponse('Sync logtime success!')