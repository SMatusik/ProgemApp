import uuid
from django.db import models

from invitation.managers import ProjectInvitationManager


class ProjectInvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    project = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    target_user_email = models.EmailField()
    created_by = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    objects = ProjectInvitationManager()

    def __str__(self):
        return f"invitation to {self.project.name} for email: {self.target_user_email}"
