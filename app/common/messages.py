from enum import Enum


class LoginMessages:
    SUCCESS = "You have been logged in"
    FAILURE = "Incorrect login data provided. Try again"

class RegisterMessages:
    SUCCESS = "You have been successfully registered"
    FAILURE = "Incorrect registration data provided. Try again"
    USER_ALREADY_EXISTS= "User with provided email already exists"

class LogoutMessages:
    SUCCESS = "You have been successfully logged out"

class InvitationMessages:
    INVITED_TO_PROJECT = "User {username} has been invited to your project"
    ALREADY_SENT = "Invitation to {project_name} has been already sent"
    NO_INVITATIONS = "You have got no pending invitations"
    ACCEPTED = "Invitation to {project_name} has been accepted. Now you have access to this project"
    DECLINED = "You've successfully declined invitation"
    REVOKED = "Invitation to {email} has been revoked"

class MessageText:
    REGISTER = RegisterMessages
    LOGIN = LoginMessages
    LOGOUT = LogoutMessages
    INVITATION = InvitationMessages

    TEST= "Teeest!"