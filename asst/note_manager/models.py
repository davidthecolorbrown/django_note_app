from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # for returning instance of a new Note

# table to store list of categories
class Category(models.Model):
    name = models.CharField(max_length=20)

    # return string representation of category 
    def __str__(self):
        return self.name

# table to store individual notes
#class Post(models.Model):
class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # auto_now_add assigns curr data/time to this field whenever instance is created 
    last_modified = models.DateTimeField(auto_now=True) # auto_now assigns curr date/time to field whenever instance is SAVED (edits)
    categories = models.ManyToManyField('Category', related_name='notes') # link categories/notes (many-to-many) using djangos ManytoManyField type 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, default=.get_or_create(pk=1))
    #author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    # method for getting url for note
    def get_absolute_url(self):
        # reverse() returns full path as string 
        return reverse('note_detail', kwargs={'pk': self.pk}) 

    # method to return the author of this post object
    #def get_author():
        #return Note.objects.get_or_create(id=1)
        #return Note.objects.get_or_create(pk=1)

# 
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey('Note', on_delete=models.CASCADE)

# 
