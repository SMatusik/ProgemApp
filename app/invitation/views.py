from uuid import UUID

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from invitation.models import ProjectInvitation
from project.models import Project

from common.messages import MessageText


@login_required
def create_invitation(request: HttpRequest, project_id: UUID) -> HttpResponse:
    project = Project.objects.filter(uuid=project_id).first()

    if request.method == "POST":
        target_email = request.POST.get("target_email")
        invitation = ProjectInvitation.objects.filter(
            Q(project_id=project_id) &
            Q(target_user_email=target_email) &
            Q(active=True)
        ).first()

        if not invitation:
            new_invitation = ProjectInvitation(
                project=project,
                target_user_email=target_email,
                created_by=request.user,
            )
            new_invitation.save()
            messages.success(
                request=request,
                message=MessageText.INVITATION.INVITED_TO_PROJECT.format(username=target_email)
            )
        else:
            messages.error(request=request, message=MessageText.INVITATION.ALREADY_SENT.format(project_name=project.name))

        return redirect("view_project", project_id)
    else:
        return render(request, "create_invitation.html", {"project": project})


@login_required
def list_invitations_for_user(request: HttpRequest) -> HttpResponse:
    invitations = ProjectInvitation.objects.filter(
        Q(target_user_email=request.user.email) & Q(active=True)
    )
    if not invitations:
        messages.warning(request=request, message=MessageText.INVITATION.NO_INVITATIONS)

    return render(request, "list_invitations.html", {"invitations": invitations})


@login_required
def list_invitations_for_project(request, project_id: UUID):
    # TODO check for users not belonging to project
    pass
    # invitations = ProjectInvitation.objects.filter(
    #     Q(uuid=invitation_id) & Q(target_user_email=user.email) & Q(active=True)
    # ).first()
    # invitations = ProjectInvitation.objects.filter()
    # return render(request, "list_invitations.html", {"invitations": invitations})


@login_required
def accept_invitation(request, invitation_id: UUID):
    user = request.user
    invitation = ProjectInvitation.objects.filter(
        Q(uuid=invitation_id) & Q(target_user_email=user.email) & Q(active=True)
    ).first()
    project = Project.objects.filter(Q(uuid=invitation.project.uuid)).first()

    invitation.accepted = True
    invitation.active = False

    project.users.add(user)

    invitation.save()
    project.save()

    messages.success(
        request=request,
        message=MessageText.INVITATION.ACCEPTED.format(project_name=project.name),
    )

    return redirect("view_project", invitation.project.uuid)


@login_required
def decline_invitation(request, invitation_id: UUID):
    user = request.user
    invitation = ProjectInvitation.objects.filter(
        Q(uuid=invitation_id) & Q(target_user_email=user.email)
    ).first()

    invitation.accepted = False
    invitation.active = False
    invitation.save()

    messages.success(
        request=request, message=MessageText.INVITATION.DECLINED
    )

    return redirect("list_user_invitations")


@login_required
def revoke_invitation(request, invitation_id: UUID):
    invitation = ProjectInvitation.objects.filter(
        Q(uuid=invitation_id)
    ).first()

    invitation.active = False
    invitation.save()

    messages.success(
        request=request, message=MessageText.INVITATION.REVOKED.format(email=invitation.target_user_email)
    )

    return redirect("view_project", invitation.project.uuid)
