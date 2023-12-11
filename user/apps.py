from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"


# class CustomModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
#     }
#
# admin.site.register(YourModel, YourModelAdmin)