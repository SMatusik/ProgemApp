
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from uuid import UUID

from .models import ProjectInvitation

from project.models import Project


@login_required
def create_invitation(request, project_id: UUID):
    project = Project.objects.filter(uuid=project_id).first()

    if request.method == 'POST':
        target_email = request.POST.get("target_email")
        user = request.user

        new_invitation = ProjectInvitation(
            project=project,
            target_user_email=target_email,
            created_by=user,
        )
        new_invitation.save()

        return redirect("view_project", project_id)
    else:
        return render(request, 'create_invitation.html', {"project": project})


@login_required
def list_invitations_for_user(request):
    user = request.user
    invitations = ProjectInvitation.objects.filter(
        Q(target_user_email=user.email) &
        Q(active=True)
    )
    return render(request, 'list_invitations.html', {'invitations': invitations})


@login_required
def list_invitations_for_project(request, project_id: UUID):
    # TODO check for users not belonging to project
    invitations = ProjectInvitation.objects.filter(
        Q(uuid=invitation_id) &
        Q(target_user_email=user.email) &
        Q(active=True)
    ).first()
    invitations = ProjectInvitation.objects.filter()
    return render(request, 'list_invitations.html', {'invitations': invitations})


@login_required
def accept_invitation(request, invitation_id: UUID):
    user = request.user
    invitation = ProjectInvitation.objects.filter(
        Q(uuid=invitation_id) &
        Q(target_user_email=user.email) &
        Q(active=True)
    ).first()
    project = Project.objects.filter(Q(uuid=invitation.project.uuid)).first()

    invitation.accepted = True
    invitation.active = False

    project.users.add(user)

    invitation.save()
    project.save()

    return redirect("view_project", invitation.project.uuid)


@login_required
def decline_invitation(request, invitation_id: UUID):
    user = request.user
    invitation = ProjectInvitation.objects.filter(Q(uuid=invitation_id) & Q(target_user_email=user.email)).first()

    invitation.accepted = False
    invitation.active = False
    invitation.save()

    return redirect("list_user_invitations")
