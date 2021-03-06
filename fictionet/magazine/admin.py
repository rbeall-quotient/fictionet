from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from magazine.models import profile, Story, Favorite

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class StoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','last_updated',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Favorite)
