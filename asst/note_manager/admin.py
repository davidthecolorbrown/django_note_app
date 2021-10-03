from django.contrib import admin
#from blog.models import Post, Category
from note_manager.models import Note, Category

#class PostAdmin(admin.ModelAdmin):
class NoteAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)
#admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)