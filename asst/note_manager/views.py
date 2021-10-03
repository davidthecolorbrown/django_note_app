from django.shortcuts import render
#from blog.models import Post, Comment
from note_manager.models import Note, Comment
from .forms import CommentForm

def note_index(request):
    notes = Note.objects.all().order_by('-created_on')
    context = {
        "notes": notes,
    }
    return render(request, "note_index.html", context)


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

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(note=note)
    context = {
        "note": note,
        "comments": comments,
        "form": form,
    }

    return render(request, "note_detail.html", context)


    # add create functionality 

    # add delete functionality 

    # add update functionality 