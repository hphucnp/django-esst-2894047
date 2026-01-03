from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
from .models import Note

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/smart/notes'

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class PopularNoteListView(ListView):
    context_object_name = "notes"
    template_name = "notes/popular_notes_list.html"
    def get_queryset(self):
        return Note.objects.filter(likes__gt=1)

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"

def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})