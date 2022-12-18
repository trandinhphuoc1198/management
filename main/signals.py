from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import LogTime,Task
from django.db.models import F

@receiver(post_save,sender=LogTime)
def logtime_created(sender,instance,created,**kwargs):
    task = Task.objects.get(pk=instance.task_id_id)
    task.spent_time=F('spent_time')+instance.spent_time
    task.save()
    if parent_task := task.parent_task_id:
        parent_task.spent_time=F('spent_time')+instance.spent_time
        parent_task.save()
        if grand_task := parent_task.parent_task_id:
            grand_task.spent_time=F('spent_time')+instance.spent_time
            grand_task.save()
      