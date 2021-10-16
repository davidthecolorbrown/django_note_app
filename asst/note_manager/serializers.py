# serializers.py
from rest_framework import serializers
from note_manager.models import Note, Category

# 
class NoteSerializer(serializers.ModelSerializer):
    # 
    class Meta:
        model = Note
        fields = ('id', 'author', 'title', 'body', 'created_on', 'last_modified', 'categories')
        #fields = ('title', 'body')
