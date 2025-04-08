from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class List(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(to=Board, on_delete=models.CASCADE)
    position = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    color = models.CharField(max_length=50)


class TaskLabel(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    list = models.ForeignKey(to=List, on_delete=models.CASCADE)
    due = models.DateTimeField()
    position = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(to=TaskLabel)


class TaskComment(models.Model):
    # user =
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
