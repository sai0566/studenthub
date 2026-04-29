from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
class CustomUser_admin(UserAdmin):
    fieldsets= UserAdmin.fieldsets+(('Role information',{'fields':('role',)}),)

    add_fieldsets=UserAdmin.add_fieldsets+(('Role information',{'fields':('role',)}),)

    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

    list_filter=['role']
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser,CustomUser_admin)

