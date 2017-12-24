from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100)

class ToDoListItem(models.Model):
    todo_list = models.ForeignKey('ToDoList', related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
