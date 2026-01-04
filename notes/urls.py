from django.urls import path

from . import views

urlpatterns = [
    path("notes", views.NoteListView.as_view(), name="note.list"),
    path("popular-notes", views.PopularNoteListView.as_view()),
    path("notes/<int:pk>", views.NoteDetailView.as_view(), name="note.detail"),
    path("notes/<int:pk>/edit", views.NoteUpdateView.as_view(), name="note.update"),
    path("notes/<int:pk>/delete", views.NoteDeleteView.as_view(), name="note.delete"),
    path("notes/new", views.NoteCreateView.as_view(), name="note.new"),
    path("notes/<int:pk>/like", views.like, name="note.like"),
    path(
        "notes/<int:pk>/change_visibility", views.change_visibility, name="note.change_visibility"
    ),
]
