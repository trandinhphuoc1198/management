from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import LogTime,Task
from django.db.models import F
from datetime import datetime
from pytz import timezone

@receiver(post_save,sender=LogTime)
def logtime_created(sender,instance,created,**kwargs):
    if created:
        task = Task.objects.get(pk=instance.task_id_id)
        task.spent_time=F('spent_time')+instance.spent_time
        task.note = instance.comments
        task.updated_date = timezone('Asia/Ho_Chi_Minh').localize(datetime.now())
        task.save()
        if parent_task := task.parent_task_id:
            parent_task.spent_time=F('spent_time')+instance.spent_time
            parent_task.save()
            if grand_task := parent_task.parent_task_id:
                grand_task.spent_time=F('spent_time')+instance.spent_time
                grand_task.save()
