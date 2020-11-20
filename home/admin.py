from django.contrib import admin
from .models import Post, Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','subject', 'email')
