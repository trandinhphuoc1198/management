from main.models import *
from .models import *
from django.http import HttpResponse
from datetime import datetime,timedelta
from pytz import timezone
from django.db import IntegrityError


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
            persons_to_management.append(Person(id=person.id,name=f'{person.firstname} {person.lastname}'))
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
        
        return HttpResponse('Sync meta data success')
    except Exception as e:
        return HttpResponse(e)


def sync_task(request,days=7):
    days=int(days)
    print(days)
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

    tz = timezone('Asia/Ho_Chi_Minh')
    point_of_time_to_sync = tz.localize(datetime.now() - timedelta(days=days))
    taskes_from_redmine = Issues.objects.filter(updated_on__gte=point_of_time_to_sync).order_by('created_on')
    taskes_to_management = []
    for task in taskes_from_redmine:
        project_id = Garage_Sales if task.project_id in [MarketPlace_Staff_Tool,MarketPlace_API,MarketPlace,WebikeGarageSale] else (Shiten if task.project_id != Common_Project else Other)
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
                'category_id' : task.project_id,
                'note' : None,
                'spent_time' : 0,
                'estimate_time' : task.estimated_hours,
                'created_date' : task.created_on,
                'updated_date' : task.updated_on
            })
    retry = True
    while retry:
        retry = False
        for task in taskes_to_management:
            print(task)
            try:
                Task.objects.update_or_create(pk=task['id'],defaults=task)
            except IntegrityError:
                retry = True
            except Exception as e:
                print('=============',task['id'],'==============')
                return HttpResponse(e)
    print(len(taskes_to_management))
    return HttpResponse('Sync task success!')


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
        except Exception as e:
            print('=============',logtime['id'],'==============')
            return HttpResponse(e)
    return HttpResponse('Sync logtime success!')