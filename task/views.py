from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from uuid import UUID

from project.models import Project
from task.models import Task


@login_required
def create_task(request):
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

        new_task = Task(
            name=name,
            description=description,
            started=started,
            finished=finished,
            end_date=end_date,
            created_by=user,
        )

        new_task.save()
        # Redirect or render success message
        return redirect("create")
    else:
        # Render the form to create a new project
        return render(request, 'create_project.html')


@login_required
def view_task(request, task_id: UUID):
    user = request.user
    project = Project.objects.filter(
        Q(users=user)
    ).first()

    task = Task.objects.filter(
        Q(uuid=task_id) &
        Q(project=project)
    ).first()
    
    return render("view_task", {"task": task})


@login_required
def edit_task(request, task_id: UUID):
    pass


@login_required
def delete_task(request, task_id: UUID):
    user = request.user
    project = Project.objects.filter(
        Q(users=user)
    ).first()
    
    Task.objects.filter(
        Q(uuid=task_id) &
        Q(project=project)
    ).delete()
    
    return redirect("view_project", project.uuid)
