from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NoteForm

# Create your views here.
from .models import Note


class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/smart/notes"


class NoteUpdateView(UpdateView):
    model = Note
    success_url = "/smart/notes"
    form_class = NoteForm


class NoteCreateView(CreateView):
    model = Note
    success_url = "/smart/notes"
    form_class = NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"
    login_url = "/admin"

    def get_queryset(self):
        # Using Note.objects.filter to avoid Pylance type errors with reverse relationships
        return Note.objects.filter(user=self.request.user)


class PopularNoteListView(ListView):
    context_object_name = "notes"
    template_name = "notes/popular_note_list.html"

    def get_queryset(self):
        return Note.objects.filter(likes__gt=1)


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"


def like(request, pk: int):
    # note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        Note.objects.filter(pk=pk).update(likes=F("likes") + 1)
        return HttpResponseRedirect(reverse("note.detail", args=(pk,)))
    raise Http404
