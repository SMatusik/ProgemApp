from django.urls import path
from invitation import views

urlpatterns = [
    path(
        "create/<uuid:project_id>/", views.create_invitation, name="create_invitation"
    ),
    path("user_list/", views.list_invitations_for_user, name="list_user_invitations"),
    path(
        "project_list/",
        views.list_invitations_for_project,
        name="list_project_invitations",
    ),
    path(
        "accept/<uuid:invitation_id>", views.accept_invitation, name="accept_invitation"
    ),
    path(
        "decline/<uuid:invitation_id>",
        views.decline_invitation,
        name="decline_invitation",
    ),
    path(
        "revoke/<uuid:invitation_id>",
        views.revoke_invitation,
        name="revoke_invitation",
    ),
]
