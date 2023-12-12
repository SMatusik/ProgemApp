from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'assignee', 'story_points']
        labels = {
            'name': 'Task Name',
            'description': 'Description',
            'assignee': 'Assignee',
            'story_points': 'Story Points',
        }
