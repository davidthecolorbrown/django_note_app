from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView
)
from . import views

urlpatterns = [
    # function views
    path("", views.note_index, name="note_index"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
    path("<category>/", views.note_category, name="note_category"),
    path("new/<int:pk>/", views.note_create, name="note_create"),

    # class views
    #path("", NoteListView.as_view(), name="note_index"), # class view route
    #path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"), # class view route
    #path("new/", NoteCreateView.as_view(), name="note_create"), # class view route
]