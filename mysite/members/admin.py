from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_no', 'role', 'club')
    list_filter = ('club', 'role')
