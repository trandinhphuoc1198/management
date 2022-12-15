from django.db import models

class Task_Status(models.Model):
    status = models.TextField()

    def __str__(self) -> str:
        return self.status

class Task_Type(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.type

class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    project = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.status

class Task_Category(models.Model):
    category = models.CharField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.category


class Task(models.Model):
    task_id = models.CharField(max_length=255)
    task_title = models.CharField(max_length=255)
    status = models.ForeignKey(Task_Status,on_delete=models.RESTRICT)
    parent_task_id = models.ForeignKey('self',null=True,on_delete=models.RESTRICT)
    description = models.CharField(max_length=1000,default='')
    target_date=models.DateTimeField(null=True)
    type= models.ForeignKey(Task_Type,on_delete=models.RESTRICT)
    priority = models.IntegerField(default=0)
    person_in_charge = models.ForeignKey(Person,on_delete=models.RESTRICT)
    project = models.ForeignKey(Project,on_delete=models.RESTRICT)
    category = models.ForeignKey(Task_Category,on_delete=models.RESTRICT)
    note = models.CharField(max_length=1000,null=True)
    spent_time = models.IntegerField(default=0)
    estimate_time = models.IntegerField(default=0)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.task_title