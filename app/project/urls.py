from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create_project, name="create"),
    path("list/", views.list_projects, name="list_projects"),
    path("view/<uuid:project_id>/", views.view_project, name="view_project"),
    path("edit/<uuid:project_id>/", views.edit_project, name="edit_project"),
    path("delete/<uuid:project_id>/", views.delete_project, name="delete_project"),
    path("unassign/<uuid:project_id>/user/<uuid:user_id>/", views.delete_user_from_project, name="unassign_user")
]
