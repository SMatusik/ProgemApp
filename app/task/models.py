import uuid
from enum import Enum

from django.db import models

from .managers import TaskManager


class TaskState(Enum):
    DONE = "DONE"
    IN_REVIEW = "IN REVIEW"
    PROGRESS = "PROGRESS"
    TO_DO = "TO DO"
    NEEDS_DISCUSSION = "NEEDS DISCUSSION"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value



    @classmethod
    def state_order(cls):
        return {
            cls.TO_DO.value: 10,
            cls.NEEDS_DISCUSSION.value: 20,
            cls.PROGRESS.value: 30,
            cls.IN_REVIEW.value: 40,
            cls.DONE.value: 50,
        }



class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.TextField(("name"), max_length=50)
    description = models.TextField(("description"), max_length=250)

    reporter = models.ForeignKey(
        "user.CustomUser", on_delete=models.DO_NOTHING, related_name="reporter"
    )
    assignee = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.DO_NOTHING,
        related_name="assignee",
        null=True,
        blank=True,
    )

    project = models.ForeignKey(
        "project.Project", on_delete=models.CASCADE, related_name="tasks"
    )

    date_created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    state = models.CharField(
        choices=[(state.value, state.name) for state in TaskState],
        default=TaskState.TO_DO.value,
    )

    story_points = models.IntegerField(default=0)
    objects = TaskManager()

    def __str__(self):
        return f"task: {self.name} in project: {self.project.name}"

    @staticmethod
    def get_available_states():
        return list([task_state.value for task_state in TaskState])

    def get_state_display(self):
        return self.state

