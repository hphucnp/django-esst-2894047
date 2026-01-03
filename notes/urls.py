from django.urls import path
from . import views


urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('popular-notes', views.PopularNotesListView.as_view()),
    path('notes/<int:pk>', views.NoteDetailView.as_view())
]