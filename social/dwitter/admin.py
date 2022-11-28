from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile,Dweet

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inline =[ProfileInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)
#admin.site.register(Profile)
