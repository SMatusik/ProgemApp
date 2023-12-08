from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def projects_view():
    pass