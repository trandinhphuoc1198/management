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
        return self.project

class Task_Category(models.Model):
    category = models.CharField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.RESTRICT,null=True)
    category_parent = models.ForeignKey('self',on_delete=models.RESTRICT,null=True)

    def __str__(self) -> str:
        return self.category

class Activity(models.Model):
    activity = models.CharField(max_length=100)

class Task(models.Model):
    task_title = models.CharField(max_length=255)
    status = models.ForeignKey(Task_Status,on_delete=models.RESTRICT)
    done_ratio = models.IntegerField(default=0)
    parent_task_id = models.ForeignKey('self',null=True,on_delete=models.RESTRICT)
    description = models.TextField(default='')
    target_date=models.DateField(null=True)
    type= models.ForeignKey(Task_Type,on_delete=models.RESTRICT)
    priority = models.IntegerField(default=0)
    person_in_charge = models.ForeignKey(Person,on_delete=models.RESTRICT,null=True)
    project = models.ForeignKey(Project,on_delete=models.RESTRICT)
    category = models.ForeignKey(Task_Category,on_delete=models.RESTRICT)
    note = models.CharField(max_length=1000,null=True,default='')
    spent_time = models.FloatField(default=0)
    estimate_time = models.FloatField(null=True)
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()

    def __str__(self) -> str:
        return self.task_title

class LogTime(models.Model):
    person = models.ForeignKey(Person,on_delete=models.RESTRICT)
    activity = models.ForeignKey(Activity,on_delete=models.RESTRICT)
    task_id = models.ForeignKey(Task,on_delete=models.RESTRICT)
    spent_time = models.FloatField(default=0)
    comments = models.TextField(null=True)
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()