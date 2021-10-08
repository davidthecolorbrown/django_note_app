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

# homepage, displays all notes
def note_index(request):
    notes = Note.objects.all().order_by('-created_on')
    context = {
        "notes": notes,
    }
    return render(request, "note_index.html", context)

# displays notes by categories
def note_category(request, category):
    notes = Note.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "notes": notes
    }
    return render(request, "note_category.html", context)

# shows details of notes
def note_detail(request, pk):
    note = Note.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                note=note
            )
            comment.save()

    comments = Comment.objects.filter(note=note)
    context = {
        "note": note,
        "comments": comments,
        "form": form,
    }

    return render(request, "note_detail.html", context)

# TODO: updating a note
def note_update(request, pk):
    notes = Note.objects.all().order_by('-created_on')
    context = {
        "notes": notes,
    }
    return render(request, "note_index.html", context)

# TODO: deleting a note
def note_delete(request, pk):
    notes = Note.objects.all().order_by('-created_on')
    context = {
        "notes": notes,
    }
    return render(request, "note_index.html", context)





# class view (same as note_index)
class NoteListView(LoginRequiredMixin, ListView):
#class NoteListView(LoginRequiredMixin, UserPassesTestMixin,  ListView):
    model = Note
    template_name = 'note_index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-created_on']
    login_url = "/admin" # redirected to this url if not logged in (instead of 404)
    
    # method to only return notes for logged in (authenticated) user
    def get_queryset(self):
        # get User object that has username equal to passed url query parameters or return 404 if user doesn't exist ('kwargs' == html query parameters)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return the filtered notes by author and display newest notes first 
        return Note.objects.filter(author=user).order_by('-created_on')
    
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

# class for viewing individual notes 
class NoteDetailView(LoginRequiredMixin, DetailView):
#class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'note_detail.html'  # <app>/<model>_<viewtype>.html
    #context_object_name = 'notes'
    
    # method to only return notes for logged in (authenticated) user
    def get_queryset(self):
        # get User object that has username equal to passed url query parameters or return 404 if user doesn't exist ('kwargs' == html query parameters)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return the filtered notes by author and display newest notes first 
        return Note.objects.filter(author=user).order_by('-created_on')
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
    success_url = '/'

    # check that person trying to change post is author of post
    def test_func(self):
        note = self.get_object()
        # user is original author of post
        if self.request.user == note.author:
            return True
        # not original author of post, return '403 forbidden'
        return False
