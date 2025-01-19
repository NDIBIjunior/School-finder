from django.contrib import admin
from .models import School, Level, Exam
from django.contrib.auth.admin import UserAdmin
from .models import Owner

# Register your models here.

admin.site.register(School)
admin.site.register(Level)
admin.site.register(Exam)


class OwnerAdmin(UserAdmin):
    model = Owner
    list_display = ('email', 'first_name', 'last_name' ,'is_active', 'is_staff')
    ordering = ('email',)
    search_fields = ('email', 'first_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('nom', 'téléphone', 'date_de_naissance')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Owner, OwnerAdmin)
