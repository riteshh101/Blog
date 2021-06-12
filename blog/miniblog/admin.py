from django.contrib import admin
from .models import Post,contact
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','uname','time']
@admin.register(contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','desc']