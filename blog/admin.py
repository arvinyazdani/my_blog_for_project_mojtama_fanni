from django.contrib import admin
from . models import Comment, Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","slug","status","published")
    list_filter = ('status','published','creat')
    search_fields = ('title','body')
    ordering = ('status','published')
    date_hierarchy = 'published'
    prepopulated_fields = {'slug':('title',)}
    row_id_fields = ('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','creat_at','status')
    list_filter = ('status','creat_at','update_at')
    search_fields = ('name','email','body')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','sen','id_number','phone')
    list_filter = ('is_writor','gener','sen')
    search_fields = ('user','phone','id_number')
