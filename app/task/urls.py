from django.urls import path
from . import views

urlpatterns = [
    path("project/<uuid:project_uuid>/create_task/", views.create_task, name="create_task"),
    # path("list/", views.list_projects, name="list_projects"),
    path("view/<uuid:task_id>/", views.view_task, name="view_task"),
    path("edit/<uuid:task_id>/", views.edit_task, name="edit_task"),
    path("delete/<uuid:task_id>/", views.delete_task, name="delete_task"),
]
