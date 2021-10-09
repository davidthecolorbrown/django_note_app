from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView
)
from . import views
#from users import views as user_views # import users views

urlpatterns = [
    # function views (allows all users to see, create, update, and delete notes)
    path("", views.note_index, name="note_index"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
    path("<category>/", views.note_category, name="note_category"),
    #path("post/new/", views.note_create, name="note_create"),
    #path("<int:pk>/update/", views.note_update, name="note_update"),
    #path("<int:pk>/delete/", views.note_delete, name="note_delete"),

    # class views 
    #path("<str:user>", NoteListView.as_view(), name='note_index'), # class view for display ONLY notes for the logged in user 
    path('user/<str:username>', NoteListView.as_view(), name='note_index'), # class view for display ONLY notes for the logged in user 
    #path("user/<str:username>/<int:pk>", NoteDetailView.as_view(), name="note_detail"), # class view route
    #path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"), # class view route
    path("post/new/", NoteCreateView.as_view(), name="note_create"), # class view route
    path("<int:pk>/update", NoteUpdateView.as_view(), name="note_update"), # class view route
    path("<int:pk>/delete", NoteDeleteView.as_view(), name="note_delete"), # class view route

    # class views (allows only users logged into see, create, update, and delete notes)
    #path('user/<str:username>', NoteListView.as_view(), name='note_index'), # class view for display ONLY notes for the logged in user 
    #path("user/<str:username>/<int:pk>", NoteDetailView.as_view(), name="note_detail"), # class view route
    #path("post/new/", NoteCreateView.as_view(), name="note_create"), # class view route
    #path("user/<str:username>/<int:pk>/update", NoteUpdateView.as_view(), name="note_update"), # class view route
    #path("user/<str:username>/<int:pk>/delete", NoteDeleteView.as_view(), name="note_delete"), # class view route
]