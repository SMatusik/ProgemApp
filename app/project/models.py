import uuid

from django.db import models

from .managers import ProjectManager


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.TextField(("name"), max_length=50)
    description = models.TextField(("description"), max_length=250)

    started = models.BooleanField(default=True)
    finished = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)

    created_by = models.ForeignKey(
        "user.CustomUser", on_delete=models.CASCADE, related_name="created_by"
    )
    users = models.ManyToManyField("user.CustomUser", related_name="users")
    super_users = models.ManyToManyField("user.CustomUser", related_name="superusers")

    objects = ProjectManager()

    def __str__(self):
        return self.name
