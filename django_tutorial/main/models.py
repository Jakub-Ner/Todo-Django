from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_list", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    completed = models.BooleanField()
    opening_date = models.CharField(max_length=50)
    closing_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.text
