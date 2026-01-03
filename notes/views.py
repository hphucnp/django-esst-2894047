from django.http import Http404
from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView
)

from .forms import NoteForm

# Create your views here.
from .models import Note

class NoteUpdateView(UpdateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NoteForm

class NoteCreateView(CreateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NoteForm

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"

class PopularNoteListView(ListView):
    context_object_name = "notes"
    template_name = "notes/popular_note_list.html"
    def get_queryset(self):
        return Note.objects.filter(likes__gt=1)

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"

