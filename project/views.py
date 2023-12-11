from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from uuid import UUID

from invitation.models import ProjectInvitation
from task.models import Task
from .models import Project


@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        started, finished = False, False
        if request.POST.get("started", False):
            started = True
        if request.POST.get("finished", False):
            finished = True

        end_date = request.POST.get('end_date')

        if end_date == "":
            end_date = None

        user = request.user

        new_project = Project(
            name=name,
            description=description,
            started=started,
            finished=finished,
            end_date=end_date,
            created_by=user,
        )

        new_project.save()
        new_project.super_users.add(user)
        # Redirect or render success message
        return redirect("create")
    else:
        # Render the form to create a new project
        return render(request, 'create_project.html')


@login_required
def list_projects(request):
    user = request.user
    projects = Project.objects.filter(Q(users=user) | Q(super_users=user))
    return render(request, 'list_projects.html', {'projects': projects})


@login_required
def view_project(request, project_id: UUID):
    project = Project.objects.filter(uuid=project_id).first()

    invitations = ProjectInvitation.objects.filter(Q(project=project) & Q(active=True)).all()
    tasks = Task.objects.filter(Q(project=project)).all()
    context = {
        "project": project,
        "invitations": invitations,
        "tasks": tasks
    }

    return render(request, 'view_project.html', context)

@login_required
def edit_project(request, project_id: UUID):
    project = Project.objects.filter(uuid=project_id).first()

    return render(request, 'view_project.html', {'project': project})


@login_required
def delete_project(request, project_id: UUID):
    project = Project.objects.filter(uuid=project_id).first().delete()

    return redirect('list_projects')
