from django.db import models


class CreateTask(models.Model):
    Name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.id
