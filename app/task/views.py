from uuid import UUID

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from project.models import Project
from task.forms import TaskForm
from task.models import Task


@login_required
def create_task(request, project_uuid: UUID):
    project = Project.objects.get(uuid=project_uuid)
    form = TaskForm(request.POST or None)
    form.fields["assignee"].queryset = project.users.all() | project.super_users.all()

    if request.method == "POST":
        if form.is_valid():
            user = request.user
            new_task = Task(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                reporter=user,
                assignee=form.cleaned_data["assignee"],
                project=project,
                story_points=form.cleaned_data["story_points"],
            )
            new_task.save()

            messages.success(request=request, message=f"Task has been created.")
            return redirect("view_project", project_id=project.uuid)

    context = {
        "form": form,
    }
    return render(request, "create_task.html", context)


@login_required
def view_task(request, task_id: UUID):
    user = request.user
    project = Project.objects.filter(Q(users=user) | Q(super_users=user)).first()

    task = Task.objects.filter(Q(uuid=task_id) & Q(project=project)).first()

    return render(request, "view_task.html", {"task": task})


@login_required
def edit_task(request, task_id: UUID):
    pass


@login_required
def delete_task(request, task_id: UUID):
    user = request.user

    task = Task.objects.filter(Q(uuid=task_id)).first()
    project = Project.objects.filter(Q(users=user) | Q(id=task.project.id)).first()

    if task:
        task.delete()
        messages.success(
            request=request, message=f"Task {task.name} has been deleted from a project"
        )

    return redirect("view_project", project.uuid)
