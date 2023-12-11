from django.db import models

import uuid
from django.db import models

from .managers import TaskManager


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.TextField(("name"), max_length=50)
    description = models.TextField(("description"), max_length=250)

    reporter = models.ForeignKey("user.CustomerUser", on_delete=models.DO_NOTHING)
    assignee = models.ForeignKey("user.CustomerUser", on_delete=models.DO_NOTHING)

    project = models.ForeignKey("project.Project", on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)

    story_points = models.IntegerField(default=0)
    objects = TaskManager()

    def __str__(self):
        return f"task: {self.name} in project: {self.project.name}"

