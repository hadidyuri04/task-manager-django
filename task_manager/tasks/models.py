from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title= models.CharField(max_length=100)
    assigned_to=models.ForeignKey(User, on_delete=models.CASCADE,related_name='assigned_tasks')
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_tasks')
    description=models.TextField(blank=True,null=True)
    Status_choice=[('Pending','Pending'),('In Progress','In Progress'),('Completed','Completed'),]
    status=models.CharField(max_length=20,choices=Status_choice,default='Pending')
    created_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    def __str__(self):
        return self.title