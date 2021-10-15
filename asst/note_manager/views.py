from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from note_manager.models import Note, Comment
#from .forms import CommentForm, NoteForm
from .forms import CommentForm, NoteForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets
from .serializers import NoteSerializer

# displays notes by categories for only the logged in user
@login_required
def note_category(request, category):
    # get and display ONLY the logged in users notes at index
    user = request.user # get logged in user from request
    # return filtered notes by author AND category passed in request
    notes = Note.objects.filter(
        categories__name__contains=category,
        author=user
    ).order_by('-created_on')

    # return notes by category for ALL users
    #notes = Note.objects.filter(
    #    categories__name__contains=category
    #).order_by(
    #    '-created_on'
    #)

    #
    context = {
        "category": category,
        "notes": notes
    }
    return render(request, "note_category.html", context)

# class view (same as note_index)
class NoteListView(LoginRequiredMixin, ListView):
#class NoteListView(LoginRequiredMixin, UserPassesTestMixin,  ListView):
    model = Note
    template_name = 'note_index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-created_on']
    login_url = "/admin" # redirected to this url if not logged in (instead of 404)
    #log#

    # create pagination for page 
    paginate_by = 4

    # check that person trying to change post is author of post
    def test_func(self):
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            #return True
            return Note.objects.filter(author=user).order_by('-created_on')
        # not original author of post, return '403 forbidden'
        return False
    
# class for viewing individual notes 
class NoteDetailView(LoginRequiredMixin, DetailView):
#class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'note_detail.html'  # <app>/<model>_<viewtype>.html

    # check that person trying to change post is author of post
    def test_func(self):
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            #return True
            return Note.objects.filter(author=user).order_by('-created_on')
        # not original author of post, return '403 forbidden'
        return False

# class view (same as note_category)
class NoteCategoryView(LoginRequiredMixin, ListView):
#class NoteategoryView(LoginRequiredMixin, UserPassesTestMixin,  ListView):
    model = Note
    template_name = 'note_category.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-created_on']
    login_url = "/admin" # redirected to this url if not logged in (instead of 404)
    #log#

    # create pagination for page 
    paginate_by = 4

    # check that person trying to change post is author of post
    def test_func(self):
        self.kwargs['category']
        #
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            #return True
            #return Note.objects.filter(author=user).order_by('-created_on')
            return Note.objects.filter(
                #categories__name__contains=category,
                #categories__name__contains=self.kwargs['category'],
                categories=self.kwargs['category'],
                author=user
            )
        # not original author of post, return '403 forbidden'
        return False

# 
class NoteCreateView(LoginRequiredMixin, CreateView):
#class NoteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Note
    #fields = ['title', 'content']
    #fields = ['content']
    fields = ['title', 'body', 'categories']
    #form_class = NoteForm
    #fields = '__all__'
    template_name = 'note_create.html'  # <app>/<model>_<viewtype>.html

    # when submitting form, set the logged in user as the person who submitting, then verify form is valid
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    '''
    # check that person trying to change post is author of post
    def test_func(self):
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            return True
        # not original author of post, return '403 forbidden'
        return False
    '''

#
class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'body', 'categories']
    template_name = 'note_create.html'  # <app>/<model>_<viewtype>.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check that person trying to change post is author of post
    def test_func(self):
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            return True
        # not original author of post
        return False

# 
class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/note_manager'
    #success_url = '/note_manager/user/' + note.author

    # check that person trying to change post is author of post
    def test_func(self):
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            return True
        # not original author of post, return '403 forbidden'
        return False





# API views #

# API endpoint for notes (GET/POST/UPDATE/DELETE)
# URL: 
    # collection: './note_manager/api/notes/'
    # element: './note_manager/api/notes/<id>'
class NoteViewSet(viewsets.ModelViewSet):
    # query all notes and order most recently created first 
    queryset = Note.objects.all().order_by('-created_on')
    # serialize as json 
    serializer_class = NoteSerializer

# API endpoint for categories (GET/POST/UPDATE/DELETE)
# URL: 
    # collection: './note_manager/api/notes/'
    # element: './note_manager/api/notes/<id>'