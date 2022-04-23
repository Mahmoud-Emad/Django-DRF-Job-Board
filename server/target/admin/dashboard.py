from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib import admin

from server.target.models import *




class UserAdminChangeForm(UserChangeForm):
    """
    handle the admin dashboard list fields
    """
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['id']
    form = UserAdminChangeForm
    list_display = ('id', 'email', 'full_name', 'is_active', 'user_type','last_login')
    
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name','password',
            'last_name', 'user_type', 'is_admin',
            'is_active', 'is_staff', 'is_superuser','groups')
            }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin',
            'is_active', 'is_staff', 'is_superuser', 'first_name',
            'last_name', 'groups', 'user_type'),
        }),
    )

    search_fields = ('id', 'first_name', 'last_name', 'user_type', 'email')

    list_filter = ('is_active', 'is_superuser', 'user_type')


class JobSeekerAdmin(admin.ModelAdmin):
    model = JobSeeker
    search_fields = ['email', 'full_name']
    list_display = (
        'id', 'email', 'full_name', 'city','phone','is_active','last_login'
    )
    readonly_fields = ['last_login', 'created', 'modified']
    fieldsets = (
        (None, {
            'fields': (
                'email','first_name','last_name','phone',
                'country','city','description'
                )
            }
        ),
    )


class EmployerAdmin(admin.ModelAdmin):
    model = Employer
    search_fields = ['email', 'full_name']
    list_display = (
        'id', 'email', 'full_name', 'company_name','company_size','is_active','last_login'
    )
    readonly_fields = ['last_login', 'created', 'modified']
    fieldsets = (
        (None, {
            'fields': (
                'email','first_name','last_name','phone',
                'company_name','company_size','description'
                )
            }
        ),
    )


class JobAdmin(admin.ModelAdmin):
    model = Job
    search_fields = ['email', 'full_name', 'company__company_name']
    list_display = (
        'id','title','fullname', 'company_name','closed', 'created_at'
    )
    readonly_fields = ['created', 'modified']
    fieldsets = (
        (None, {
            'fields': (
                'title','experience','job_type','company',
                'country','city','applied_users','description'
                )
            }
        ),
    )
