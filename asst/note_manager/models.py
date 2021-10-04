from django.db import models
from django.urls import reverse # for returning instance of a new Note

# table to store list of categories
class Category(models.Model):
    name = models.CharField(max_length=20)

# table to store individual notes
#class Post(models.Model):
class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # auto_now_add assigns curr data/time to this field whenever instance is created 
    last_modified = models.DateTimeField(auto_now=True) # auto_now assigns curr date/time to field whenever instance is SAVED (edits)
    #categories = models.ManyToManyField('Category', related_name='posts') # link categories/notes (many-to-many)
    categories = models.ManyToManyField('Category', related_name='notes') # link categories/notes (many-to-many) using djangos ManytoManyField type 

    # method for getting url for note
    def get_absolute_url(self):
        # reverse() returns full path as string 
        return reverse('note_detail', kwargs={'pk': self.pk}) 

#
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #post = models.ForeignKey('Post', on_delete=models.CASCADE)
    note = models.ForeignKey('Note', on_delete=models.CASCADE)

# 
