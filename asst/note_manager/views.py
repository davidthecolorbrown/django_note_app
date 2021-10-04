from django.shortcuts import render
#from blog.models import Post, Comment
from note_manager.models import Note, Comment
from .forms import CommentForm, NoteForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# 
def note_index(request):
    notes = Note.objects.all().order_by('-created_on')
    context = {
        "notes": notes,
    }
    return render(request, "note_index.html", context)


# 
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

# 
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

# 
#def note_create(request):
def note_create(request, pk):
    note = Note.objects.get(pk=pk)

    form = CommentForm() 
    '''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    '''
    #comments = Comment.objects.filter(note=note)
    #comments = Comment.objects.all()
    comments = Note.objects.all()
    context = {
        "note": note,
        "comments": comments,
        "form": form,
    }

    return render(request, "note_create.html", context)


# class view (same as note_index)
class NoteListView(ListView):
    model = Note
    template_name = 'note_index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-created_on']

# class for viewing individual notes 
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'  # <app>/<model>_<viewtype>.html
    #context_object_name = 'notes'

#class NoteCreateView(LoginRequiredMixin, CreateView):
class NoteCreateView(CreateView):
    model = Note
    #fields = ['title', 'content']
    #fields = ['content']
    template_name = 'note_create.html'  # <app>/<model>_<viewtype>.html

    # when submitting form, set the logged in user as the person who submitting, then verify form is valid
    '''#def form_valid(self, form):
        #form.instance.author = self.request.user
        #return super().form_valid(form)'''
