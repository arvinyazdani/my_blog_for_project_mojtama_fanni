from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','sen','id_number','phone')
    list_filter = ('is_writor','gener','sen')
    search_fields = ('user','phone','id_number')
