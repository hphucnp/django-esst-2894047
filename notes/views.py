from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
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


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = "/smart/notes"
    form_class = NoteForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return Note.objects.filter(Q(user=self.request.user) | Q(is_public=True))


class PopularNoteListView(ListView):
    context_object_name = "notes"
    template_name = "notes/popular_note_list.html"

    def get_queryset(self):
        return Note.objects.filter(
            Q(user=self.request.user) | Q(is_public=True), likes__gt=1
        )


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"


@login_required
def like(request, pk: int):
    if request.method == "POST":
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse("note.detail", args=(pk,)))
    raise Http404


@login_required
def make_public(request, pk: int):
    if request.method == "POST":
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.is_public = True
        note.save()
        return HttpResponseRedirect(reverse("note.detail", args=(pk,)))
    raise Http404
