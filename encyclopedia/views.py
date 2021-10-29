from django.shortcuts import render
from django import forms

from . import util
# from wiki import encyclopedia

# view for home page


class NewEntryForm(forms.Form):
    t = forms.CharField(label="Title")
    c = forms.TextField(label="Content")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# view for entry page
# got data but still needs to be formated


def entry_view(request, entry):
    entryContent = util.get_entry(entry)
    if entryContent:
        return render(request, "encyclopedia/entry.html", {"entryTitle": entry.upper, "entryContent": entryContent})
    else:
        return render(request, "encyclopedia/error.html")


def search_view(request):
    entry = request.POST["q"]
    entryContent = util.get_entry(entry)
    if entryContent is not None:
        return render(request, "encyclopedia/entry.html", {"entryTitle": entry.upper, "entryContent": entryContent})
    else:
        return render(request, "encyclopedia/search.html", {"entry": entry, "entries": util.list_entries()})


def new_entry_view(request):
    form = NewEntryForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
    return render(request, "encyclopedia/new_entry.html")
