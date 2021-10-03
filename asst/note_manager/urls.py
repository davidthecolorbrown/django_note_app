from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_index, name="note_index"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
    path("<category>/", views.note_category, name="note_category"),
]