from django.urls import path, include
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    NoteCategoryView
)
from . import views
#from users import views as user_views # import users views

# api framework stuff 
from rest_framework import routers
#from django.urls import include

# router for creating API endpoint urls 
router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet, 'notes') # get notes

# 
urlpatterns = [
    path('', NoteListView.as_view(), name='note_index'), # class view for display ONLY notes for the logged in user 
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"), # class view route
    path("<category>/", views.note_category, name="note_category"),
    #path("<category>/", NoteCategoryView.as_view(), name="note_category"), # class view route
    path("post/new/", NoteCreateView.as_view(), name="note_create"), # class view route
    path("<int:pk>/update", NoteUpdateView.as_view(), name="note_update"), # class view route
    path("<int:pk>/delete", NoteDeleteView.as_view(), name="note_delete"), # class view route

    # api views 
    #path('api/', include(router.urls)),
    #path('api/notes/', include(router.urls)),
    path('note_manager/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]